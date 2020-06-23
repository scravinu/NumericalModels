#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 22:37:27 2020

@author: Sharad
"""

#@author Sharad
#Step1: Import libraries
import matplotlib.pyplot as plt
import numpy as np

#Step2: Declaring system parameters 
ndays = 200
dt = 1                    #time step in days
beta = (1.0/3.0)          #infection rate [1 person per 3 days] (only change the denominator number)
gamma = (1.0/14.0)        #recovery rate [14 days] (only change the denominator number)
epsilon = (1.0/14.0)      #incubation rate [14 days] (only change the denominator number)
myu = (1/8)              #rate of death
v = 4/200                 #Vaccination rate
N = 1                    #Number of people, value to be kept at unity if dealing with fraction of population

#Step3: setting model parameters
S = np.zeros(ndays)       #susceptible population 
E = np.zeros(ndays)       #Exposed population
I = np.zeros(ndays)       #infective popluation
R = np.zeros(ndays)       #recovered population
D = np.zeros(ndays)       #dead population
V = np.zeros(ndays)       #vaccinated population
t = np.arange(ndays)*dt 

I[0] = 0.005*N              #inital infective population
E[0] = 0                  #inital exposed population
S[0] = (1 - I[0])*N           #inital susceptible 
D[0] = 0
V[0] = 0
#Step4: Run the simulation 
for i in range(ndays -1):

#SEIR
#  S[i+1] = S[i] - (beta*S[i]*I[i])*dt
#  E[i+1] = E[i] + (beta*S[i]*I[i] - epsilon*E[i])*dt
#  I[i+1] = I[i] + (epsilon*E[i] - gamma*I[i])*dt
#  R[i+1] = R[i] + gamma*I[i]*dt
  
#SIRD
#  S[i+1] = S[i] - (beta*S[i]*I[i])*dt
#  #E[i+1] = E[i] + (beta*S[i]*I[i] - epsilon*E[i])*dt
#  I[i+1] = I[i] + (beta*S[i]*I[i] - gamma*I[i] - myu*I[i])*dt
#  R[i+1] = R[i] + gamma*I[i]*dt
#  D[i+1] = D[i] + (myu * I[i])*dt

#SVEIRD
 S[i+1] = S[i] - (beta*S[i]*I[i]/N + v*S[i])*dt
 E[i+1] = E[i] + (beta*S[i]*I[i]/N - epsilon*E[i])*dt
 I[i+1] = I[i] + (epsilon*E[i] - gamma*I[i])*dt
 R[i+1] = R[i] + (gamma*(1-myu)*I[i]+v*S[i])*dt
 D[i+1] = D[i] + (myu *gamma* I[i])*dt
 V[i+1] = V[i] + v*S[i]*dt
 
 

#Step5: Plot the graph
fig = plt.figure(1); fig.clf()
plt.plot(t, S, color='green', lw=3, label ='Susceptible')
plt.plot(t, V, color='pink', lw=4, label ='Vaccinated')
plt.plot(t, E, color='purple', lw=3, label ='Exposed')
plt.plot(t, I, color ='red', lw=3, label ='Infected')
plt.plot(t, R, color ='blue', lw=3, label ='Recovered')
plt.plot(t, D, color ='black', lw=3, label ='Dead')
fig.legend(); plt.xlabel('Days'); plt.ylabel('Fraction of Population')