"""
Entry point for all the 'invoke' tasks
"""
from tasks.test import *
from invoke import Collection

namespace = Collection()
namespace.add_collection(test)