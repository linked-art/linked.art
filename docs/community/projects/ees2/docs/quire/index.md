---
title: ""
---
[Back to EES2 Project page](https://linked.art/community/projects/ees2/)

# Quire Linked Art Extension

The Quire Linked Art Extension enables the retrieval and ingestion of Linked Art data and IIIF images via Quire’s command-line interface, seamlessly merging them into a Quire project. It interacts with Linked Art records through their URIs, streamlining processes that previously required manual data entry. The video below showcases the extension’s functionality, demonstrating its use with Linked Art records accessed via the LUX and Getty APIs.

<div style="text-align: center;">
  <iframe width="560" height="315" src="https://www.youtube.com/watch?v=XEzPBwicQAg" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</div>

00:00 - Adding an object from a Linked Art resource  
02:30 - Adding a figure from a Linked Art resource to an existing object  
04:00 - Adding a figure from a Linked Art resource  
05:22 - Choosing what fields to retrieve  
07:00 - Processing multiple Linked Art records in a single command  
08:15 - Using a Linked Art activity URI to add all objects featured in an exhibition  
09:30 - Choosing fields interactively and previewing entries  
10:29 - Generating a spreadsheet of all data in a Linked Art record  
11:30 - Resizing an image upon retrieval  
12:40 - Selectively importing objects from an activity record based on object type and artist name  
14:10 - Running native build, pdf, and epub commands  

## Quire Linked Art Extension Installation

The Quire Linked Art Extension is available on the [releases](https://github.com/oerc-csi/la-quire/releases) page of the EES2 project's GitHub repository. In the 'Assets' dropdown of the latest version, click on the 'js-files.zip' link to download.

Once you have downloaded the Quire Linked Art Extension, visit our [Training](https://linked.art/community/projects/ees2/docs/training) page for installation instructions.

## Quire Linked Art Extension Documentation

The Linked Art command class for Quire is called `add`. Information about Quire’s command classes can be accessed by running `quire help` in the terminal. `add` is listed as follows:

`add [options] <thing> <uri> [id1] [id2]  Fetch Linked Art`

All commands begin with `quire`. To run the `add` command, start by typing `quire add` in the terminal. The elements that follow `quire add` are arguments and options. The arguments and options included in the command determine what the software will do. Those in angled brackets are required, and those in square brackets are optional (except for `[id1]` when adding a figure to an existing object, see section 1.2)

### **1 Arguments**

There are four arguments: `<thing>`, `<uri>`, `[id1]`, and `[id2]`.  
`<thing>` can be `object`, `object.figure`, `figure`, or `spreadsheet`.  
`<uri>` should be a Linked Art URI for one of the following types of records: HumanMadeObject, DigitalObject, or Activity.  
`[id1]` and `[id2]` can be any string, or the word `accession` can be passed to use the accession number of the object as the ID.  
The following sections explain how these arguments are used in commands to accomplish specific tasks.

#### **1.1 Adding an object to objects.yaml**

To add an object to objects.yaml, run:

`quire add object <uri>`

Optionally, the user can create their own ID for the object by running:

`quire add object <uri> [id1]`

If the user does not pass an ID, one will be automatically generated. The ID can be any string that is not already being used as an ID. The accession number of the object can be retrieved and used as the ID by passing the word `accession` as `[id1]`.

#### **1.2 Adding a figure to an existing object in objects.yaml**

To add a figure to an existing object in objects.yaml, run:

`quire add object.figure <uri> [id1]`

`[id1]` is required here because the program needs to know which object to add the figure to. `[id2]` is optional and works the same way `[id1]` does when adding an object to objects.yaml.

`quire add object <uri> [id1] [id2]`

#### **1.3 Adding a figure to figures.yaml**

To add a figure to figures.yaml run:

`quire add figure <uri> [id1]`

As usual, a unique ID or the word `accession` can be passed as [id1]. If an ID is not provided, one will be generated.

#### **1.4 Browse all Linked Art data for an object in a spreadsheet**

The `spreadsheet` arg provides a way for the user to easily browse Linked Art by generating a CSV file containing all the fields of a Linked Art record and their values/contents in the project folder.

`quire add spreadsheet <uri>`

### **2 Choosing fields, field order, and field names**

The user has the ability to choose which fields are retrieved from the Linked Art record, the order in which they are displayed, and their names. Field selection and order are handled by the object_display_order section of the objects.yaml file, and field names can be changed from defaults in the objectFieldNames section of the config.yaml file.

#### **2.1 objects.yaml object_display_order**

There are 21 fields currently supported by the Linked Art extension in addition to object title, which is always retrieved:

Creator  
Type  
Year  
Period  
Dimensions  
Materials  
Location  
Accession  
Credit line  
Set  
Owner  
Took place at  
Encountered by  
Find spot  
Access statement  
Linked Art URI  
Web Page  
Thumbnail Link  
Description  
Citations  
Provenance  

To choose fields to retrieve and their order of appearance, simply include them in the object_display_order list in the desired order. The fields are rendered with the same names and in the same order as they appear in this section.

**IMPORTANT:** the field names in the object_display_order section of objects.yaml must match the names provided in the objectFieldNames section of config.yaml

#### **2.2 config.yaml objectFieldNames**

The user can choose the names of the fields by changing the default names in config.yaml. The  following are the internal names (left) and default/chosen names (right) as they appear in config.yaml:

objectFieldNames:  
creator: creator  
type: type  
year: year  
period: period  
dimensions: dimensions  
materials: materials  
location: location  
accession: accession  
creditLine: credit line  
set: set  
owner: owner  
tookPlaceAt: took place at  
encounteredBy: encountered by  
encounterPlace: find spot  
accessStatement: access statement  
uri: linked art uri  
webPage: web page  
thumbnailImg: thumbnail link  
description: description  
citations: citations  
provenance: provenance  

The internal names should not be changed, as these are mapped for the successful retrieval of Linked Art data. To change a field name, change the value assigned to the internal name here in the objectFieldNames section of config.yaml. For example:

creator: creator => creator: artist name

Remember to then change the field name in the object_display_order of objects.yaml as well.

### **3 Processing Multiple URIs and ‘activity’ URIs**

It is possible to process multiple URIs at once by passing the URIs in double quotations and separated by spaces.

`quire add object “<uri1> <uri2> … <uriN>”`

It is also possible to process multiple URIs by passing a URI of a Linked Art record of the ‘activity’ type. An ‘activity’ in Linked Art, such as an exhibition, can involve multiple objects. To begin processing all the objects in an ‘activity’ record, run a command as it were any other type of record:

`quire add <thing> <uri>`

The program will detect that the URI is an ‘activity’ URI and start an interaction:

`The provided URI is of type 'Activity' and may be used to access a set of object URIs.`  
`Enter 'p' to process all the objects in the set.`  
`Enter 's' to generate a spreadsheet of information about the objects.`  
`Enter 'b' to do both.`  

After a selection is made, the program will process all the objects in the ‘activity’ record and/or generate a spreadsheet of information about the objects.

### **4 Options**

There are two options: `--dry-run` and `--force`.

#### **4.1 Preview an entry before adding to objects.yaml or figures.yaml**

The user has the option to preview an entry before it is added to objects.yaml or figures.yaml by using the `--dry-run` option. When `--dry-run` is passed, an entry will not be added and an image will not be downloaded. Instead, the entry will be logged in the console for the user to see.

`quire add <thing> <uri> [id1] [id2] --dry-run`

#### **4.2 Refetching Linked Art and overwriting cache**

When the user runs commands that retrieve Linked Art data and figures, the data and figure hashes will be added to caches. When a URI that has been passed is passed again, the program will retrieve Linked Art data from the cache instead of making new http requests to refetch the data.

The user has the ability to change the fields they wish to retrieve as they work on their project. Therefore, there could be cases where the user passes a URI they have passed before, but wishes to retrieve fields that are not in the cache. The ‘--force’ option allows the user to ignore cache and refetch Linked Art to retrieve the desired fields. The cache entry for the URI is rewritten.

`quire add <thing> <uri> [id1] [id2] --force`

#### **4.3 Resizing images**

By default, full-size images of objects are retrieved. The `--resize` option allows the user to resize images if they wish to download a version with a smaller file size.

`quire add <thing> <uri> [id1] [id2] --resize`

When ‘--resize’ is passed, an interaction will start:

`Enter the number or percentage of pixels for resizing (e.g., 800 for pixels, or 50% for percentage). This will be applied to the largest dimension (width or height), and the other dimension will be scaled proportionally.`  
`The largest dimension is [dimension] at [number] pixels.`

After entering the number or percentage of pixels for resizing, the image will be resized accordingly before being downloaded as usual.

#### **4.4 Selecting fields in interactive mode**

The primary method of selecting the fields to be retrieved is by including the field names in the object_display_list at the top of the objects.yaml file. The `--interactive` option provides an alternative way of making this selection.

`quire add <thing> <uri> [id1] [id2] --interactive`

When `--interactive` is passed, an interaction will start:

`Interactive Linked Art entry building has been initialized.`  
`Choose the Linked Art data fields you would like to retrieve by entering a comma-separated list.`  
`Note: object title and Linked Art URI are always included in the entries and therefore are not present in the list of options.`  
`artist, type, year, period, dimensions, materials, location, accession, credit line, set, owner, took place at, encountered by, find spot, access statement, web page, thumbnail link, description, citations, provenance`

After entering a comma-separated list of fields, the module disregards the object_display_order and retrieves the fields in the list in the order they were provided.