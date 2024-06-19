from django.shortcuts import render,redirect
from .forms import EmployeeForm
from .models import Employee

# Create your views here.
def testFn(request):
    name='coding'
    return render(request,'emp/test.html',{'name':name})

def details(request):
    college='Islington'
    list=[2,3,4,5]
    return render(request,'emp/deal.html',{'college':college,'list':list})

def empoyee(request):
    first_name='Binod Thapa'
    salary= 923234
    age=23
    return  render(request,'emp.html',{'Name':first_name,'Salary':salary,'Age ':age})


def saveEmp(request):
    if request.method == "POST":  # Check if the request method is POST
        form = EmployeeForm(request.POST)  
        if form.is_valid():  # Check if form data is valid
            form.save()  # Save the form data to the database
            return redirect('success.html')  # Redirect 
    else:
        form = EmployeeForm()  
    
    return render(request, 'emp/emp.html', {'form': form})


def success(request):
    return render(request,'emp/success.html')


# def saveEmp(request):

#     if request.method == "POST":  # Use request.method to check for POST request
#         form = EmployeeForm(request.POST)  # Bind POST data to the form
#         if form.is_valid():  # Check if the form data is valid
#             form.save()  # Save the form data to the database
#         return redirect('success.html')  # Redirect to a success page or another view
#     else:
#         form = EmployeeForm()  # If not a POST request, create a blank form instance
    
#     return render(request, 'emp/emp.html', {'form': form})
#         # if form =="POST":
#         #     form.save()
#         # form=EmployeeForm()
        
#         # return render(request,'emp/emp.html',{'form':form})
    