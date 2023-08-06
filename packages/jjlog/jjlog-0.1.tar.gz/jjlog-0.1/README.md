## <b>📚  About</b>
Centralize log for Python with:
- UTC time with ISO8601 format.
- Accency to milliseconds.
- Json format.
- Log write to console
- Log write to specific file location and rotate (optional) 

## <b>📝  Usage</b>

```python

from jjlog import jjlogger

log = jjlogger("jjapp Log", "./log/jjapp.log")
# log = jjlogger("jjapp Log")   ## Or just output to console
logger = log.getLogger()

logger.info("jj test001")
```
Output: `{ 'time':'2022-03-27T14:07:17.456Z','name':'jjapp Log','level':'INFO','message':'log start' }`


## <b>🔧 Examples:</b>
[example code](https://gitlab.com/mhliu8/jjlog/-/tree/main/tests)