import os


from typing import List


datapath: str = os.path.abspath(
    os.path.join(os.path.dirname(__file__), os.path.pardir, "data/")
)
__all__: List[str] = ["datapath"]
