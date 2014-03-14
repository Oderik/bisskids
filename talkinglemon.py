from bottle import route, run, debug, template, request


@route('/say', method='GET')
def say():
    text = request.GET.get('text', '')
    return text

@route('/count', method='GET')
def count():
    limit = request.GET.get('limit', 10)

    result = ""
    for number in range(1, int(limit) + 1):
        result += str(number) + ", "

    return result

run(port=80)