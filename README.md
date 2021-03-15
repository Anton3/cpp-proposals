## Generator

The proposals use the [Bikeshed](https://tabatkins.github.io/bikeshed) generator. To start:

- Clone the repository
- Install Python 3 with the [requirements](generator/requirements.txt)
- Install VS Code with the [Bikeshed](https://marketplace.visualstudio.com/items?itemName=kainino.bikeshed) plugin
- Open the repository in VS Code using "Open folder"

The [draft](draft) directory contains `.bs` sources and `.html` renders. The "Build" VS Code task is set up to compile the currently open `.bs` file and put the `.html` render next to it.

The [published](published) directory contains final versions of the proposals submitted to WG21.

## Proposals

To view any of the proposals in the browser, find its HTML on GitHub and paste the URL into [GitHack](https://raw.githack.com).

| ID      | Name                                             | Description                                                  | Link                                                         |
| ------- | ------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| P2025R0 | Guaranteed copy elision for named return objects | Guaranteed copy elision for local variables being returned from a function | [Link](https://rawcdn.githack.com/Anton3/cpp-proposals/db611c48ca00752969ea03f2d39ef77e5a11e132/draft/d2025r0.html)
| P2025R1 | Guaranteed copy elision for return variables | Guaranteed copy elision for local variables being returned from a function, a.k.a. "guaranteed NRVO". | [Link](https://rawcdn.githack.com/Anton3/cpp-proposals/1244583dcc326519134d46a5c8f27b2735fb7904/published/p2025r1.html)
| P2025R2 | Guaranteed copy elision for return variables | Guaranteed copy elision for local variables being returned from a function, a.k.a. "guaranteed NRVO". | [Link](https://rawcdn.githack.com/Anton3/cpp-proposals/bd3061f731fbdecf1e20379090d147fa1c6ac8f6/published/p2025r2.html) |
