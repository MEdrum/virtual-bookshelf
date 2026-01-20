from django.shortcuts import render

def loan_requests_overview(request):
    return render(request, "pages/loan_requests_overview.html", {})

# # Create your views here.
# def loan_requests_overview(request):
#     projects = Project.objects.all()
#     context = {
#         "projects": projects
#     }
#     return render(request, "projects/project_index.html", context)

# def project_detail(request, pk):
#     project = Project.objects.get(pk=pk)
#     context = {
#         "project": project
#     }
#     return render(request, "projects/project_detail.html", context)