{% extends "mail_templated/base.tpl" %}

{% block subject %}
Hello {{ user }}
{% endblock %}

{% block body %}

{% endblock %}

{% block html %}
<h3>hi {{ user }},</h3>
<h4>You are reaching the due time</h4>
<p>This email is just a reminder.</p>
{% endblock %}