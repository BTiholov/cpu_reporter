from datetime import datetime
from typing import List, Tuple
import matplotlib.pyplot as plt
import sys
import io
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders


def plain_text_format(report: List[Tuple[datetime, int]]):
    return '\n'.join([
        time.strftime('%H:%M:%S.%f') + ' ' + str(measurement)
        for time, measurement in report
    ])


def line_chart_format(report):
    time = [time for time, _ in report]
    measurements = [measurement for _, measurement in report]

    f = plt.figure()
    plt.plot(time, measurements, color='Blue')
    plt.xlabel('Time')
    plt.ylabel('CPU Percentage Load')
    plt.title('CPU Report')
    binary = io.BytesIO()
    f.savefig(binary, bbox_inches='tight', format='png')
    binary.seek(0)

    email = MIMEMultipart()
    part = MIMEBase("application", "octet-stream")

    part.set_payload(binary.read())

    encoders.encode_base64(part)

    part.add_header('Content-Disposition', 'attachment; filename="%s"' % 'report.png')

    email.attach(part)
    return email


