import clang.cindex

if __name__ == "__main__":
    buf = f"""
import clang.cindex
# Autogenerated enum class for IDE autocomplete
from enum import Enum
  """

    for klazz in clang.cindex.BaseEnumeration.__subclasses__():
        buf += f"""
class {klazz.__name__}(Enum):
  def __eq__(self, other):
    \"\"\"Overrides the default implementation\"\"\"
    if isinstance(other, clang.cindex.{klazz.__name__}):
        return self.name == other.name
    return NotImplemented
    """
        for kind in [x for x in klazz._kinds if not x is None]:
            buf += (
                f"\n  {kind.name} = clang.cindex.{klazz.__name__}.from_id({kind.value})"
            )
        buf += "\n"

    with open("clang_base_enumerations.py", "w+") as f:
        f.write(buf)
