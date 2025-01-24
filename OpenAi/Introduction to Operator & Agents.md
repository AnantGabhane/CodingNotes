Agents :
- AI agents are the systems that can do the work for you independently
- you give them a task and they go do it

Operator :
- A system that can use a web browser in the cloud that can accomplish a task that you give it 
- Operator can control the mouse and keyboard and do all sorts of things 

Workflow of the operator:
- As soon as you give it a prompt(query) for e.g. book me a table at bertta at 7pm today
- Operator instantiates a completely remote browser. It's running in the cloud somewhere. AI is clicking around
- Task delegation is also available. Then comes task confirmation before taking the critical action
- Operator is based on model computer usign agents (COLA) - AGI

Operator safety and mitigations:
- The operator is not allowed to do harmful tasks like buying a weapon
- If agent is misaligned then main mitigatation is confirmation 
- If website is misaligned then main mitigatation is model try to avoid following that instruction if that also fails then there is separate layer on the top of it called prompt ingestion monitor (Antivirus) if finds anything suspicious then it pauses it. 