from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Job, JobApplicant
from .forms import JobApplicantForm

# Example queryset: jobObjor = Job.objects.filter(job_title__icontains="foo")

def job_list(request):
    query = request.GET.get("q")
    jobs = Job.objects.all()
    if query:
        jobs = jobs.filter(job_title__icontains=query) | jobs.filter(
            job_description__icontains=query
        ) | jobs.filter(location__icontains=query)
    return render(request, "jobs/job_list.html", {"jobs": jobs})

@login_required
def job_detail(request, pk):
    job = get_object_or_404(Job, pk=pk)
    if request.user.is_admin:
        applicants = JobApplicant.objects.filter(job=job)
        return render(
            request,
            "jobs/job_detail_admin.html",
            {"job": job, "applicants": applicants},
        )
    else:
        form = JobApplicantForm()
        return render(
            request,
            "jobs/job_detail_user.html",
            {"job": job, "form": form},
        )

class JobUpdateView(UpdateView):
    model = Job
    fields = ["job_title", "job_description", "min_offer", "max_offer", "location"]
    template_name = "jobs/job_update.html"
    success_url = reverse_lazy("jobs:job_list")

class JobDeleteView(DeleteView):
    model = Job
    template_name = "jobs/job_delete.html"
    success_url = reverse_lazy("jobs:job_list")

@login_required
def apply_job(request, pk):
    job = get_object_or_404(Job, pk=pk)
    if request.method == "POST":
        form = JobApplicantForm(request.POST, request.FILES)
        if form.is_valid():
            applicant = form.save(commit=False)
            applicant.user = request.user
            applicant.job = job
            applicant.save()
            messages.success(request, "Your application has been submitted.")
            return redirect("jobs:job_detail", pk=job.pk)
    else:
        form = JobApplicantForm()
    return render(request, "jobs/apply.html", {"form": form, "job": job})
