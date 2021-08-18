---
title: Linked Art
---

Linked Art is a [Community](/community/) working together to create a shared [Model](/model/) based on Linked Open Data to describe Art.  We then implement that model in [Software](/software/) and use it to provide valuable content.  It is under active development and we welcome additional partners and collaborators.

Watch our recent introduction to the work from the CIDOC 2020 Conference:

<center>
<iframe width="560" height="315" src="https://www.youtube.com/embed/afO7KEysda8?start=183" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</center>

<br/>

## Want to learn more?

Beyond the documentation in the site, you can listen to some of the previous discussions of the working group on the [youtube channel](https://www.youtube.com/channel/UCNASnutgByTdQHGehoOUlSA).


<div id="devbranch" style="display:none">

<b>Development Previews</b>

<ul id="branches"></ul>
</div>

<script src="/media/vendor/gh3.js"></script>
<script>
if (window.location.hostname != "linked.art") {
	var me = new Gh3.User("linked-art");
	var larepo = new Gh3.Repository("linked.art", me);
	larepo.fetch(
		function(err, res) {
			if (err) return;
			larepo.fetchBranches(
				function(err, res) {
					if (err) return;
					// var branches = larepo.getBranches();
					larepo.eachBranch(
						function(branch) {
							if (branch.name != "master") {
								$("#branches").append('<li><a href="https://'+branch.name+
									'--linked-art.netlify.com/">'+branch.name+'</a></ul>');
								// Getting files is hard, need to walk through many commits
								// and somehow determine when to stop
							}
						}
					)					
				}
			);
			larepo.fetchPulls(
				function(err, res) {
					if (err) return;
					// var pulls = larepo.getPulls();
					larepo.eachPull(
						function(pull) {
							$("#branches").append('<li><a href="https://deploy-preview-'+pull.number+
								'--linked-art.netlify.com/">Pull Request '+pull.number+'</a>' +
								'<ul id="files_'+pull.number+'">');
							pull.fetchFiles(
								function(err, res) {
									_.each(res.files, function(file) {
										if (file.filename.startsWith("content")) {
											fn = file.filename.replace('content', '', 1)
											if (fn.endsWith(".html") || fn.endsWith(".json")) {
												$("#files_"+pull.number).append('<li><a href="https://deploy-preview-'+
													pull.number+'--linked-art.netlify.com/'+fn+'">'+fn+"</a></li>");
											}
										}
									})
								}
							);
						}
					)					
				}
			);
		}
	);
	$("#devbranch").show()
}

</script>
