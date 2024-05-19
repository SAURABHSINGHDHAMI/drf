# Introduction to Django Rest Framework (DRF)

Django Rest Framework (DRF) is a powerful and flexible toolkit for building web APIs. It is built on top of Django, a popular Python web framework, and provides a set of tools and libraries for easily creating RESTful APIs.

## What is REST?

REST stands for Representational State Transfer, which is a protocol for connecting front-end and back-end systems through APIs (Application Programming Interfaces). It allows for stateless communication between clients and servers using standard HTTP methods such as GET, POST, PUT, DELETE, etc.

## Normal Django Architecture

<p align="center">
  <img src="https://media.licdn.com/dms/image/D4D12AQHJ1cxt7KSCzA/article-inline_image-shrink_1500_2232/0/1669119151475?e=1721865600&v=beta&t=WZx4o-vibpCD-ogDspM7AGTs4ZYqBxMJBY87hqdqOL4" alt="drf">
</p>

In a typical Django application, the architecture follows a Model-View-Template (MVT) pattern where the model represents the data, the view handles the presentation logic, and the template manages the rendering of the user interface.

## Django Rest Framework Architecture

<p align="center">
  <img src="https://www.nileshdalvi.com/images/post/django-framework/architecture_huabcd77374b052d2e58d3b97c783a0aeb_94780_1271x0_resize_q100_h2_box.webp" alt="drf">
</p>

When integrating Django with DRF, the architecture adapts to accommodate the RESTful API structure. DRF introduces serializers, views, and routers to handle requests and responses in a RESTful manner.

## JSON (JavaScript Object Notation)

JSON is a lightweight data-interchange format that is easy for humans to read and write and easy for machines to parse and generate. It is commonly used for transmitting data between a server and a web application as it is language-independent and self-descriptive.

<p align="center">
  <img src="https://github.com/SAURABHSINGHDHAMI/drf/assets/95751390/15f3c170-4457-4a91-be21-2342412d3d68" alt="drf">
</p>

