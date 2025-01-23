{% extends "mail_templated/base.tpl" %}

{% block subject %}
Hello {{ user }}
{% endblock %}

{% block body %}

{% endblock %}

{% block html %}
<h3>hi {{ user }},</h3>
<p>Thanks for the registration please click on link below for verification:</p>
<a href="http://127.0.0.1:8000/accounts/api/v1/verification/{{ token }}/" target=blank>Click for verification</a>
{% endblock %}