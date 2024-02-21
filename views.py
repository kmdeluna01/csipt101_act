from django.shortcuts import render
from django.http import HttpResponse

def mission(request):
    msg = "<h1>CCMS Mission</h1><br/> \
        <h3>The College of Computer Studies shall produce technically competent Information Technology professionals \
        adequately prepared in the practice of their profession supportive of national development goals and standards \
        of global excellence.</h3>"
    return HttpResponse(msg)
def vision(request):
    msg = "<h1>CCMS Vision</h1><br/> \
        <h3>The College of Computer Studies shall be a Center of Excellence in Information Technology education. </h3>"
    return HttpResponse(msg)
def obj(request):
    msg = "<H1>CCMS Program Educational Objectives</h1><br/> \
        <h3>1. Be employedd and demonstrate professionalism, competence and passion in solving contemporary computing \
        problems by developing or utilizing innovative IT solutions;<br/> \
        2. Embark in lifelong learning or research to attune to the continuos innovation in the IT industry in order to \
        adapt to the changing demands of the global market; and<br/> \
        3. Exhibit leadership and teamwork,and commitment to their respective local or global organizations.</h3>"
    return HttpResponse(msg)