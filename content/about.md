## *realfast*: real-time fast transients at the Very Large Array

Context
-----

The VLA is most sensitive cm-wavelength radio interferometer on the earth and can revolutionize the study of fast radio transients with its ability to localize sources with arcsecond spatial resolution. *realfast* will use this capability to hunt for a mysterious new class of radio transients known as [fast radio bursts](https://en.wikipedia.org/wiki/Fast_radio_burst), pulsars, and other rare astrophysical transients.

To do this, *realfast* must generate roughly 1 TB of data per hour search it in real time. This data rate is so large that it cannot be transferred via the internet for data analysis. The computing requirements are so severe that no single computer can manage the search. The question is: how can we search a TB/hour data stream for the hundreds of hours needed to find these rare transients?

<img style="border:5px solid black" width="70%" src='vla_fastimaging.png'>

Our answer is *realfast*, a system for real-time fast transient searches at the VLA via interferometric imaging. The approach was first demonstrated with the [first blind interferometric localization of a transient neutron star](http://labs.adsabs.harvard.edu/adsabs/abs/2012ApJ...760..124L) (see image above). *realfast* will scale that concept to real-time and open access to "commensal" observing in conjunction with other VLA observations.

Approach
----

*realfast* development began in late 2016 via the NSF ATI program and is based on a few key technologies:

1. **Computing hardware at the VLA**: Real-time fast transient detection requires a dedicated computing platform to search for transients.
2. **Commensal data stream**: A high-speed copy of every VLA observation can be searched for transients.
3. **Transient search pipeline**: A transient [search pipeline](http://github.com/realfastvla/rfpipe) will be implemented for GPUs.
4. **Candidate data management system**: Data products and transient alerts will be rapidly distributed to the public.

More information can be found on our [software](../software) and [services](../services) pages.

Team
----

* **Geoff Bower** (ASIAA)
* **Sarah Burke-Spolaor** (WVU)
* **Bryan Butler** (NRAO; NRAO lead)
* **Paul Demorest** (NRAO)
* **Shakeh Khudikyan** (JPL)
* **Casey Law** (UC Berkeley; Principal Investigator; claw@astro.berkeley.edu)
* **Joe Lazio** (JPL)
* **Martin Pokorny** (NRAO)
* **James Robnett** (NRAO)
* **Michael Rupen** (DRAO)

<img style="border:5px solid black" width="400" src='group_vla.jpg'>

Results and Publications
----

*realfast* publications:

1. [Law et al. (2015)](https://ui.adsabs.harvard.edu/#abs/2015ApJ...807...16L) describes a prototype *realfast* system that searched 200 hours and 200 TB of data for FRBs.
2. [Chatterjee et al. (2017)](http://dx.doi.org/10.1038/nature20797) describes how a *realfast* prototype made the first interferometric localization and host identification of an FRB (see image below).
3. [Law et al. (2017)](https://ui.adsabs.harvard.edu/#abs/2017arXiv170507553L) present a detailed analysis of radio bursts from FRB 121102.

<img style="border:5px solid black" width="70%" src='cands_16A-459_TEST_1hr.57623.72670021991_sc6-seg163-i95-dm4-dt0.png'>

*realfast* strives for openness in every aspect. Software is [open and easy to install](http://github.com/realfastvla/rfpipe), data [has and will be made available](../data) and will be made available in the future, and the [analysis behind our publications](https://github.com/caseyjlaw/FRB121102) is open.
