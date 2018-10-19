
# Semantic Versioning

We are in active development of the content at the moment, and breaking changes are to be expected as we encounter new use cases. The version of the documents is thus below 1.0, somewhere about 0.6 (if that means anything) as what we have is reasonably stable but we do not guarantee it!

# Installation Instructions

We use hyde (a Python based clone of jekyll) to manage the transformation from the easy-to-edit markdown content, into the nicely styled static HTML for the website.  We use github to manage distributed contributions and continuous deployment.

To get up and running you need python 2.7 or more recent, plus pip:

```
pip install -r requirements.txt
```

Then run `./build.sh` to generate all the example JSON-LD files and the site into .site
Note that build.sh runs `hyde gen` twice ... the second time generates only the index that is created on the first run through. 
Then run `hyde serve` to run a local webserver at http://localhost:8080/ to view the site

Commits to the master branch will auto-deploy via our hosting provider, [netlify](https://netlify.com/), to the [Linked Art](https://linked.art/) site. Going to any branch will list all of the available previews.

Pull requests from any branch, regardless of which repository they're from, will auto-deploy to previews at https://deploy-preview-NNN--linked-art.netlify.com/, where NNN is the numeric identifier of the pull request. Commits on these branches with open PRs will re-deploy the preview.

Branches on this site will auto-deploy to https://BRANCHNAME--linked-art.netlify.com/ and thus a branch named "test" would result in a preview site at https://test--linked-art.netlify.com/.

# Contributions Welcome!

Please join our discussions. How to get involved is described at: [https://linked.art/community/](https://linked.art/community/)

## Editorial Contributions

Most significant editorial changes are handled only after discussion with the community, filing of an issue and consensus around the solution.  As this work is ongoing and very active, we are not currently tracking versions of the documents individually, or backwards incompatible changes. 

Pull requests for typo corrections and other non-normative changes are very welcome from anyone.

## Technical Contributions

Technical infrastructure improvements, such as tests, coverage or other integrations, are welcome but do drop by slack to discuss them first.  Stylistic or HTML changes are the same.

### Gotchas

* If the build errors with a complaint about not being able to "generate meta", it is probably that you have a special character in the title of the document, such as a `:`. Remember that the header is actually YAML, so put the title in double quotes.

* The pymdown extras package is slightly broken with hyde at version 6.0 (late 2018), and hence we restrict the version in requirements. If some markdown functionality isn't working as expected, it could be this.


## Current Contributors

* Rob Sanderson (rsanderson@getty.edu)
* David Newbury
* Matthew Lincoln
