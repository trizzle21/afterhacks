<!DOCTYPE html>
<html lang="en">
  <head>





  <title>{% block title %}{% endblock %}</title>

    {% block head %}
    {% endblock %}


    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1">

  </head>
  <body>
    <div id="content">
    	{% block content %}
    	{% endblock %}
    </div>



  
    <div id="footer">
      Copyleft 2017 Tyler Ross   	

    </div>
    {% block tail %}
    {% endblock %}

  </body>

</html>
