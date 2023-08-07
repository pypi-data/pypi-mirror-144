import 'package:flutter/material.dart';

class ColorName {
  ColorName._();
  
  {% for color in colors %}
  static const Color hex{{ color }} = Color(0xFF{{ color }});
  {% endfor %}
}
