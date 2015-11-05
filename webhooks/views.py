from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from twilio import twiml


@require_POST
@csrf_exempt
def incoming_call(request):
    """Twilio Voice URL - receives incoming calls from Twilio"""
    # Create a new TwiML response
    resp = twiml.Response()

    # <Say> a message to the caller
    from_number = request.POST['From']
    body = """
    Thanks for calling!

    Your phone number is {0}. I got your call because of Twilio's webhook.

    Goodbye!""".format(' '.join(from_number))
    resp.say(body)

    # Return the TwiML
    return HttpResponse(resp)

@require_POST
@csrf_exempt
def incoming_message(request):
    """Twilio Messaging URL - receives incoming messages from Twilio"""
    # Create a new TwiML response
    resp = twiml.Response()

    # <Message> a text back to the person who texted us
    body = "Thanks for your text! My phone number is {0}. Webhooks are neat :)" \
        .format(request.POST['To'])
    resp.message(body)

    # Return the TwiML
    return HttpResponse(resp)
