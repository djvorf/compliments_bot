from typing import Callable


def Depends(dependency: Callable):
    return dependency()
