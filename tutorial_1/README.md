<div align="center">
<h1> Tutorial 1 </h1>
<h3>Crafting your first CrewAI Agent & Task</h3>
</div>

## Learning Objectives

- Understand the basic structure of a CrewAI Agent
- Learn how to create a simple CrewAI Task
- Understand how to set up & run a Crew

## Learning Notes

### [CrewAI Agent Attributes](https://docs.crewai.com/core-concepts/Agents/)

<table>
<tr>
<td><b>Attribute</b></td>
<td><b>Description</b></td>
</tr>
<tr>
<td>Role</td>
<td>Define the agent's function within the crew. It determines the kind of tasks the agent is best suited for.</td>
</tr>
<tr>
<td>Goal</td>
<td>The individual objective that the agent aims to achieve. It guides the agent's decision-making process.</td>
</tr>
<tr>
<td>Backstory</td>
<td>Provides context to the agent's role and goal, enriching the interaction and collaboration dynamics.</td>
</tr>
</table>


### [CrewAI Task Attributes](https://docs.crewai.com/core-concepts/Tasks/)

<table>
<tr>
<td><b>Attribute</b></td>
<td><b>Description</b></td>
</tr>
<tr>
<td>Description</td>
<td>A clear, concise statement of what the task entails.</td>
</tr>
<tr>
<td>Agent</td>
<td>The agent responsible for the task, assigned either directly or by the crew's process.</td>
</tr>
<tr>
<td>Expected Output</td>
<td>A detailed description of what the task's completion looks like.</td>
</tr>
</table>


### [CrewAI Crew Attributes](https://docs.crewai.com/core-concepts/Crews/)

<table>
<tr>
<td><b>Attribute</b></td>
<td><b>Description</b></td>
</tr>
<tr>
<td>Agents</td>
<td>A list of agents that are part of the crew.</td>
</tr>
<tr>
<td>Tasks</td>
<td>A list of tasks that the crew needs to complete.</td>
</tr>
</table>


## To Do

- [ ] Fill up the agent details in agents.py file
- [ ] Fill up the task details in tasks.py file
- [ ] Create a Crew with the agent and task
- [ ] Run the Crew
