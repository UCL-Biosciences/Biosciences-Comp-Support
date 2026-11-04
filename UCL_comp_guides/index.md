---
title: Home
layout: home
nav_order: 1
permalink: /
---

# UCL Biosciences Computational Research

Guides for navigating UCL's computational resources, from the Biosciences Data Science team. Aimed at anyone doing computational research in the Division of Biosciences.

{% assign guides = site.pages | where_exp: "p", "p.nav_order" | where_exp: "p", "p.url != page.url" | sort: "nav_order" %}
{% for p in guides %}
- [{{ p.title }}]({{ p.url | relative_url }}){% if p.description %}: {{ p.description }}{% endif %}
{% endfor %}

## Contributions
These guides are  practical summaries that help with day-to-day computational lives. We hope they will be a shared living resource and welcome suggestions and changes from all users. Please see the [contributions](https://github.com/UCL-Biosciences/Biosciences-Comp-Support/tree/main#how-do-i-contribute) section for instructions on contributing to any info in this repository.

## Get in touch

[Book a meeting with James Gilbert](https://outlook.office.com/bookwithme/user/d23d2d9663fa4276b318d8ae8f40ccbb@ucl.ac.uk/meetingtype/GP1vEk6SdU6fTvgYLBKK8Q2?anonymous&ismsaljsauthenabled&ep=mlink), Senior Research Data Scientist, or email [james.d.gilbert@ucl.ac.uk](mailto:james.d.gilbert@ucl.ac.uk).

Requests, questions or ideas: open an [issue in the repository](https://github.com/UCL-Biosciences/Biosciences-Comp-Support/issues).

UCL has a Slack workspace for computational questions: [join here](https://ucl-programming-hub.slack.com/).
