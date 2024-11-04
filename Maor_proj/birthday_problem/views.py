
# Create your views here.
# birthday_problem/views.py

from django.shortcuts import render
from .forms import BirthdayProblemForm
import numpy as np
import plotly.express as px
import plotly.io
import json

def birthday_problem_view(request):
    if request.method == 'POST':
        form = BirthdayProblemForm(request.POST)
        if form.is_valid():
            n_students = form.cleaned_data['n_students']
            perturbation = form.cleaned_data['perturbation']
            
            # Run the simulation and generate the plot
            prob_shared, plot_div = simulate_and_plot(n_students, perturbation)
            
            context = {
                'form': form,
                'probability': prob_shared,
                'plot_div': plot_div,
            }
            return render(request, 'birthday_problem/birthday_template.html', context)
    else:
        form = BirthdayProblemForm()
        context = {
            'form': form,
        }
    return render(request, 'birthday_problem/birthday_template.html', context)

def simulate_and_plot(n_students, perturbation):
    # Define monthly birth rates (simplified example)
    monthly_birth_rates = {
        'January': 0.079,
        'February': 0.076,
        'March': 0.081,
        'April': 0.08,
        'May': 0.083,
        'June': 0.081,
        'July': 0.087,
        'August': 0.089,
        'September': 0.09,
        'October': 0.087,
        'November': 0.083,
        'December': 0.085
    }

    # Number of days in each month (non-leap year)
    days_in_month = {
        'January': 31,
        'February': 28,
        'March': 31,
        'April': 30,
        'May': 31,
        'June': 30,
        'July': 31,
        'August': 31,
        'September': 30,
        'October': 31,
        'November': 30,
        'December': 31
    }

    # Create a list of days with their corresponding probabilities
    birthday_probs = []
    for month, rate in monthly_birth_rates.items():
        random_pert = np.random.normal(1, perturbation)
        num_days = days_in_month[month]
        daily_rate = rate / num_days * random_pert
        birthday_probs.extend([daily_rate] * num_days)

    # Normalize to ensure sum to 1
    birthday_probs = np.array(birthday_probs)
    birthday_probs /= birthday_probs.sum()

    # Simulate the probability
    prob_shared = simulate_non_uniform_birthdays(n_students, birthday_probs)

    # Generate the plot
    plot_div = create_plot(birthday_probs)

    return prob_shared, plot_div

def simulate_non_uniform_birthdays(n_students, birthday_probs, n_simulations=10000):
    # Precompute cumulative probabilities for efficient sampling
    cumulative_probs = np.cumsum(birthday_probs)
    
    # Initialize count of simulations with at least one shared birthday
    shared_count = 0
    
    for _ in range(n_simulations):
        # Generate n_students random birthdays based on the distribution
        random_birthdays = np.searchsorted(cumulative_probs, np.random.rand(n_students)) + 1  # Days 1-365
        
        # Check if there are duplicates
        if len(random_birthdays) != len(np.unique(random_birthdays)):
            shared_count += 1
    
    probability_shared = shared_count / n_simulations
    return probability_shared

def create_plot(birthday_probs):
    days = np.arange(1, 366)
    fig = px.bar(x=days, y=birthday_probs, labels={'x': 'Day of the Year', 'y': 'Probability'}, title='Non-Uniform Birthday Distribution')
    fig.update_layout(template='simple_white')
    plot_div = plotly.io.to_html(fig, full_html=False)
    return plot_div
