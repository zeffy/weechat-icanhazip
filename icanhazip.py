SCRIPT_NAME    = "icanhazip"
SCRIPT_AUTHOR  = "zeffy <https://github.com/zeffy>"
SCRIPT_VERSION = "1.0"
SCRIPT_LICENSE = "MIT"
SCRIPT_DESC    = "Shows your external IP using icanhazip.com"

import weechat

weechat.register(SCRIPT_NAME, SCRIPT_AUTHOR, SCRIPT_VERSION, SCRIPT_LICENSE, SCRIPT_DESC, "", "")
weechat.hook_command("icanhazip", SCRIPT_DESC, "", "", "", "icanhazip", "")

def icanhazip(data, buffer, args):
    weechat.hook_process("url:https://icanhazip.com", 5 * 1000, "icanhazip_process_cb", "")
    return weechat.WEECHAT_RC_OK

def icanhazip_process_cb(data, command, rc, out, err):
    if out != "" and int(rc) >= 0:
        weechat.prnt("", "icanhazip\tYour IP address is: %s" % out.strip())
    else:
        weechat.prnt("", "icanhazip\tThere was an error!")
    return weechat.WEECHAT_RC_OK
