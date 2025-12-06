services=[]

def fun(request):
    method,path=request.split()
    if method=="GET" and path=="/iteams":
        return services
    if method=="POST" and path=="/iteams":
        new_service={
                    "id":len(services)+1,
                     "services":"service_name"
                     }
        services.append(new_service)
        return new_service
    if method=="GET" and path.startswith("/iteams/"):
        service_id=path.split()[-1]
        return service_id
    for s in services:
        if s["id"]==service_id:
             return s
        return "no service"
    return "invalid"
a=fun({"id":4,"services":"booking"})
print(a)