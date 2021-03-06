from flask import Flask, request

from src.scripts.list_audit import ListAudit
from src.scripts.next_category import NextCategory
from src.scripts.validate_certificate import ValidateCertificate
from src.scripts.view_audit import ViewAudit

app = Flask(__name__)

@app.route('/create_audit/')
def create_audit():
    count_threads = request.args.get('count_threads', default=200, type=int)
    loop_count = request.args.get('loop_count', default=20, type=int)
    time_sleep = request.args.get('time_sleep', default=0, type=int)
    company = request.args.get('company', default=None, type=int)

    CreateAudit.run(count_threads, loop_count, time_sleep,company)

    return "Processing"

@app.route('/list_audit/')
def list_audit():
    count_threads = request.args.get('count_threads', default=200, type=int)
    loop_count = request.args.get('loop_count', default=20, type=int)
    time_sleep = request.args.get('time_sleep', default=0, type=int)

    ListAudit.run(count_threads, loop_count, time_sleep)

    return "Processing"

@app.route('/view_audit/')
def view_audit():
    count_threads = request.args.get('count_threads', default=200, type=int)
    loop_count = request.args.get('loop_count', default=20, type=int)
    time_sleep = request.args.get('time_sleep', default=0, type=int)

    ViewAudit.run(count_threads, loop_count, time_sleep)

    return "Processing"


@app.route('/next_category/')
def next_category():
    count_threads = request.args.get('count_threads', default=200, type=int)
    loop_count = request.args.get('loop_count', default=20, type=int)
    time_sleep = request.args.get('time_sleep', default=0, type=int)

    NextCategory.run(count_threads, loop_count, time_sleep)

    return "Processing"


@app.route('/validate_certificate/')
def validate_certificate():
    count_threads = request.args.get('count_threads', default=200, type=int)
    loop_count = request.args.get('loop_count', default=20, type=int)
    time_sleep = request.args.get('time_sleep', default=0, type=int)
    
    ValidateCertificate.run(count_threads, loop_count, time_sleep)
    
    return "Processing"


if __name__ == '__main__':
    app.run(host='0.0.0.0')
