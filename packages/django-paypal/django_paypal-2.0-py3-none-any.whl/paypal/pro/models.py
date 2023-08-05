#!/usr/bin/env python

from django.conf import settings
from django.db import models
from django.forms.models import model_to_dict
from django.http import QueryDict
from django.utils.functional import cached_property
from django.utils.http import urlencode

from paypal.utils import warn_untested

try:
    from idmapper.models import SharedMemoryModel as Model
except ImportError:
    Model = models.Model


class PayPalNVP(Model):
    """Record of a NVP interaction with PayPal."""

    TIMESTAMP_FORMAT = "%Y-%m-%dT%H:%M:%SZ"  # 2009-02-03T17:47:41Z
    RESTRICTED_FIELDS = [
        "expdate",
        "cvv2",
        "acct",
    ]
    ADMIN_FIELDS = [
        "id",
        "user",
        "flag",
        "flag_code",
        "flag_info",
        "query",
        "response",
        "created_at",
        "updated_at",
    ]
    ITEM_FIELDS = [
        "amt",
        "custom",
        "invnum",
    ]
    DIRECT_FIELDS = [
        "firstname",
        "lastname",
        "street",
        "city",
        "state",
        "countrycode",
        "zip",
    ]

    # Response fields
    method = models.CharField(max_length=64, blank=True)
    ack = models.CharField(max_length=32, blank=True)
    profilestatus = models.CharField(max_length=32, blank=True)
    timestamp = models.DateTimeField(blank=True, null=True)
    profileid = models.CharField(max_length=32, blank=True)  # I-E596DFUSD882
    profilereference = models.CharField(max_length=128, blank=True)  # PROFILEREFERENCE
    correlationid = models.CharField(max_length=32, blank=True)  # 25b380cda7a21
    token = models.CharField(max_length=64, blank=True)
    payerid = models.CharField(max_length=64, blank=True)

    # Transaction Fields
    firstname = models.CharField("First Name", max_length=255, blank=True)
    lastname = models.CharField("Last Name", max_length=255, blank=True)
    street = models.CharField("Street Address", max_length=255, blank=True)
    city = models.CharField("City", max_length=255, blank=True)
    state = models.CharField("State", max_length=255, blank=True)
    countrycode = models.CharField("Country", max_length=2, blank=True)
    zip = models.CharField("Postal / Zip Code", max_length=32, blank=True)

    # Custom fields
    invnum = models.CharField(max_length=255, blank=True)
    custom = models.CharField(max_length=255, blank=True)

    # Admin fields
    user = models.ForeignKey(
        getattr(settings, "AUTH_USER_MODEL", "auth.User"),
        blank=True,
        null=True,
        on_delete=models.CASCADE,
    )
    flag = models.BooleanField(default=False, blank=True)
    flag_code = models.CharField(max_length=32, blank=True)
    flag_info = models.TextField(blank=True)
    ipaddress = models.GenericIPAddressField(blank=True, null=True)
    query = models.TextField(blank=True)
    response = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "paypal_nvp"
        verbose_name = "PayPal NVP"

    @cached_property
    def response_dict(self):
        """
        Returns a (MultiValueDict) dictionary containing all the parameters returned in the PayPal response.
        """
        # Undo the urlencode done in init
        return QueryDict(self.response)

    def init(self, request, paypal_request, paypal_response):
        """Initialize a PayPalNVP instance from a HttpRequest."""
        if request is not None:
            from paypal.pro.helpers import strip_ip_port

            self.ipaddress = strip_ip_port(request.META.get("REMOTE_ADDR", ""))
            if hasattr(request, "user") and request.user.is_authenticated:
                self.user = request.user
        else:
            self.ipaddress = ""

        # No storing credit card info.
        query_data = {k: v for k, v in paypal_request.items() if k not in self.RESTRICTED_FIELDS}
        self.query = urlencode(query_data)
        self.response = urlencode(paypal_response)

        # Was there a flag on the play?
        ack = paypal_response.get("ack", False)
        if ack != "Success":
            if ack == "SuccessWithWarning":
                warn_untested()
                self.flag_info = paypal_response.get("l_longmessage0", "")
            else:
                self.set_flag(
                    paypal_response.get("l_longmessage0", ""),
                    paypal_response.get("l_errorcode", ""),
                )

    def set_flag(self, info, code=None):
        """Flag this instance for investigation."""
        self.flag = True
        self.flag_info += info
        if code is not None:
            self.flag_code = code

    def process(self, request, item):
        """Do a direct payment."""
        warn_untested()
        from paypal.pro.helpers import PayPalWPP

        wpp = PayPalWPP(request)

        # Change the model information into a dict that PayPal can understand.
        params = model_to_dict(self, exclude=self.ADMIN_FIELDS)
        params["acct"] = self.acct
        params["creditcardtype"] = self.creditcardtype
        params["expdate"] = self.expdate
        params["cvv2"] = self.cvv2
        params.update(item)

        # Create recurring payment:
        if "billingperiod" in params:
            return wpp.createRecurringPaymentsProfile(params, direct=True)
        # Create single payment:
        else:
            return wpp.doDirectPayment(params)

    def __repr__(self):
        return f"<PayPalNVP id:{self.id}>"

    def __str__(self):
        return f"PayPalNVP: {self.id}"
