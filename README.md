# free cheeseburger mike

![GitHub Workflow Status (with event)](https://img.shields.io/github/actions/workflow/status/emilydaemon/free-cheeseburger-mike/python-app.yml)
![GitHub License](https://img.shields.io/github/license/emilydaemon/free-cheeseburger-mike)

**free cheeseburger mike** is a bot that generates Discord Nitro codes
using Opera GX's promotion.

The name comes from
[this great article](https://fatprosemattrose.wordpress.com/2020/04/11/mciavellian/)
written by Matt Rose, which is a probably illegal guide on how to score yourself
some free McDonalds, with clogged arteries included.

Licensed under GPL version 3.

## How to use

Copy the config/config.def.json file to config/config.json. Make sure to
change the placeholders to the correct values.

As of December 22, 2023, the following values for gxurl and gifturl are
working:

```json
{
	"gxurl": "https://api.discord.gx.games/v1/direct-fulfillment",
	"gifturl": "https://discord.com/billing/partner-promotions/1180231712274387115/"
}
```

I recommend not creating the bot with your main Discord account, as it may
cause problems in the future if Discord starts banning people who do this.

**I am NOT liable for any potential damages, bans, etc. It's your responsibility.**
