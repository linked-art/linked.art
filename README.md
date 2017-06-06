
# Installation Instructions

We use hyde (a Python based clone of jekyll) to manage the transformation from the easy-to-edit markdown content, into the nicely styled static HTML for the website.  We use github to manage distributed contributions and continuous deployment.

To get up and running you need python 2.7 or more recent, plus pip:

```
pip install -r requirements.txt
```

Then run `./build.sh` to generate all the example JSON-LD files and the site into .site
Then run `hyde serve` to run a local webserver at http://localhost:8080/ to view the site

Commits to the master branch will auto-deploy via our hosting provider, [netlify](https://netlify.com/), to the [Linked Art](https://linked.art/) site. 

Pull requests from any other branch will auto-deploy to previews at https://deploy-preview-NNN--linked-art.netlify.com/, where NNN is the numeric identifier of the pull request. Commits on these branches with open PRs will re-deploy the preview. Branches without an open PR will not be deployed automatically.

# Contributions Welcome!

Please join our discussions. How to get involved is described at: [https://linked.art/community/](https://linked.art/community/)

## Editorial Contributions

Most significant editorial changes are handled only after discussion with the community, filing of an issue and consensus around the solution.  As this work is ongoing and very active, we are not currently tracking versions of the documents individually, or backwards incompatible changes. 

Pull requests for typo corrections and other non-normative changes are very welcome from anyone.

## Technical Contributions

Technical infrastructure improvements, such as tests, coverage or other integrations, are welcome but do drop by slack to discuss them first.  Stylistic or HTML changes are the same.

## Current Contributors

* Rob Sanderson (rsanderson@getty.edu)
* David Newbury
* Matthew Lincoln
