# Installation Instructions

```
pip install -r requirements.txt
```

Then run `./build.sh` to generate all the example JSON-LD files and the site into .site
Then run `hyde serve` to run a local webserver at http://localhost:8080/ to view the site

Commits to the master branch will auto-deploy via our hosting provider, [netlify][https://netlify.com/], to the [Linked Art][https://linked.art/] site. 

Pull requests from any other branch will auto-deploy to previews at https://deploy-preview-NNN--linked-art.netlify.com/, where NNN is the numeric identifier of the pull request. Commits on these branches with open PRs will re-deploy the preview. Branches without an open PR will not be deployed automatically.

# Contributions Welcome!

Please join our discussions. How to get involved is described at: [https://linked.art/community/][https://linked.art/community/]

# Current Contributors

* Rob Sanderson (rsanderson@getty.edu)
* David Newbury
* Matthew Lincoln
