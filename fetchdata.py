import pycurl
import json

from io import BytesIO

b_obj = BytesIO()
crl = pycurl.Curl()
crl.setopt(
    crl.URL,
    "https://api.trello.com/1/members/me/boards?key=db58ee5254120da35e6ae9a3e72029dd&token=216ba9bd2d7844ad5addfc84b90a796f35a73a3090772e6a57bb8d5d76aad712",
)
crl.setopt(crl.WRITEDATA, b_obj)
crl.perform()
crl.close()
get_body = b_obj.getvalue()
print("Output of GET request:\n%s" % get_body.decode("utf8"))
myjson = json.loads(get_body)
print("disableAt", myjson[0]["limits"]["attachments"]["perBoard"]["disableAt"])
