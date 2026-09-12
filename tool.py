import re
def audit(template:str,declared:set[str])->dict[str,list[str]]:
 used=set(re.findall(r'\{([A-Za-z_]\w*)\}',template))
 return {'undeclared':sorted(used-declared),'unused':sorted(declared-used)}
