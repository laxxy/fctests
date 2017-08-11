from invoke import task

@task
def smoke(ctx):
    """ Run tests, it just example"""
    ctx.run('pytest -v test/smoke/test1.py')
    print("running")