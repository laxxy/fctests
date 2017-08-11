from invoke import task
import os

""" Returns path to the report dir"""


def getReportPath():
    report_ = os.getcwd() + "/build/report"
    if not os.path.exists(report_):
        os.makedirs(report_)
    return report_


@task
def smoke(ctx):
    """ Run tests, it just example"""
    ctx.run('pytest -v test/smoke/test1.py --alluredir ' + getReportPath())
