:Student: Victoria Martínez de la Cruz
:Mentor: Alejandro Cabrera
:Project: `Add a new storage backend to the OpenStack Message Queuing Service`_

.. _`Add a new storage backend to the OpenStack Message Queuing Service`: https://wiki.openstack.org/wiki/GSoC2014/Queues/Storage


.. contents:: **Table of Contents**
   :depth: 2

.. sectnum::
   :suffix: .


Abstract
========

Marconi has support for two different storage engines, MongoDB_ and SQLAlchemy_. While these are great storage options, we just cannot settle with only that.

Different user needs would require different storage solutions, and being one step ahead by providing support for them is an expected feature from a software solution like Marconi.

The main goal of this proposal is to identify a storage engine that fits Marconi's interests and to implement a driver for it.


Why we want to add a new storage driver
=======================================

The current Marconi version has support for two different storage engines, MongoDB_ and SQLAlchemy_. While these are great database engine options, we just cannot settle with only that.

Different applications would require different storage solutions, and being one step ahead by providing support for them is an expected feature from a software solution like Marconi.

From the project development point of view, it would be a great addition to be used by the different `queue flavors`_ support [*]_ that will be implemented on a future release.

Besides, having more drivers will allow the Marconi community to tease out what parts of the API are hard to map.

This feature is of vital importance for the project and is being addressed by several blueprints, including:

* `Prototype Alternative Storage Drivers`_
* `High Performance Distributed Storage Driver`_
* `Redis Storage Driver`_

.. _MongoDB: http://www.mongodb.org/
.. _SQLAlchemy: http://www.sqlalchemy.org/

.. _`Prototype Alternative Storage Drivers`: https://blueprints.launchpad.net/marconi/+spec/alternative-storage-drivers
.. _`High Performance Distributed Storage Driver`: https://blueprints.launchpad.net/marconi/+spec/distributed-storage-driver
.. _`Redis Storage Driver`: https://blueprints.launchpad.net/marconi/+spec/redis-storage-driver

.. _`queue flavors`: https://blueprints.launchpad.net/marconi/+spec/marconi-queue-flavors

.. [*] Users will be able to modify queues options like durability, persistence, ordering, access and storage backend depending on their use case


Goals
=====

The main goal of this proposal is to identify a storage engine that fits Marconi's interests and to implement a driver for it, following the style of existing drivers to keep the consistency across the project.

To do this we need to do some research about the current storage engines available in the market. perform an analysis of their main features, and select one according to Marconi's goals.

The selection of the storage engine can be made considering different aspects, like performance, security, ease of use or utility.

Then we can start the development stage by writing the code for the different components of the driver, the corresponding unit tests and the associated documentation in parallel.


Benefits
========

Adding a new storage backend has many benefits. Some of them are:

* Efficiency and performance. It will be possible to deliver features needed for particular applications with a service that better fits their needs. Considering the requirements these applications may have and providing storage support for them can have a great impact on overall system efficiency and performance.

* Compatibility. Providing support for more storage alternatives will enhance the compatibility with other services, therefore simplifying the deployment.

* Scalability. It will be feasible to switch between storage solutions if the applications requirements change, improving the scalability as well.


Selecting an storage engine
===========================

Differences between databases continue to increase with the availability of many SQL, NewSQL and NoSQL alternatives. Choosing the appropriate one for a project right at the beginning is an important task.

There are several storage engines available we could take into account. Here are some possibilities classified by their purpose and popularity.


Popular storage engines
-----------------------

* `OpenStack Swift`_ - Designed to withstand hardware failures without any downtime. It is great for plenty of different applications, from small deployments for storing VM images, to mission critical storage clusters for high-volume websites. Implementing a driver for it has an added value since it would provide a better integration with OpenStack.
* RethinkDB_ - It scale to multiple machines with very little effort. Sharding and replication operations can be done in a few simple steps. It's easy to set up and learn, and it has an intuitive query language that support many useful queries like table joins, groupings, and aggregations. It is a good choice for applications that need flexible schemas and scalability. It's also great if you value ease of use and you want cluster administration to be an easier task.
* Riak_ - Focused on fault tolerance. Provides high availability and scalability. It is a great solution for applications where even seconds of downtime are unbearable.
* CouchDB_ - Its main goal is consistency and ease of use. It is usually implemented in applications where versioning is important.

.. _`OpenStack Swift`: https://wiki.openstack.org/wiki/Swift
.. _RethinkDB: http://rethinkdb.com/
.. _Riak: http://basho.com/riak/
.. _CouchDB: http://couchdb.apache.org/


Not widely known but with great features storage engines 
--------------------------------------------------------

* Couchbase_ - Memcache compatible, but with persistence and clustering. It is suitable for any application where low-latency data access, high concurrency support and high availability are required.
* VoltDB_ - It is an in-memory database intended for fast transactions and rapidly changing data. Great for applications where you need to act fast on massive amounts of incoming data.

.. _Couchbase: http://www.couchbase.com/
.. _VoltDB: http://voltdb.com/


Special purpose storage engines
-------------------------------

* ElasticSearch_ - Provides scalable search, has near real-time search, and supports multitenancy. Works like a charm when the applications deals with objects with (flexible) fields, and an advanced search functionality is needed.
* Neo4j_ - It stores data structured in graphs rather than in tables. It is ideal for storing interconnected data.

.. _ElasticSearch: http://www.elasticsearch.org/
.. _Neo4j: http://www.neo4j.org/


Implementing the driver
=======================

Given that I have MongoDB_ and SQLAlchemy_ drivers as reference models, I have a good idea of the modules that have to be implemented. For this reason I will proceed with the implementation by following a bottom-up approach. 

I will start working with queues, messages and claims controllers, continue with catalogue and shards controllers and finish with the integration of all of the implemented controllers in the driver. In the following section I list all the methods that have to be implemented - based on an inspection of `current storage backends`_ -.

It is important to write several unit tests in parallel to make sure that the code works as expected and that the implementation gets done on time. I also consider important to add detailed documentation to each controller in this stage to make the code more legible and, because of that, maintainable.

.. _`current storage backends`: https://github.com/openstack/marconi/tree/master/marconi/queues/storage


Schedule and milestones
=======================

Before start coding I want to become more familiar with the Marconi team and their workflow. To do this, I plan to:

* Discuss with the Marconi community the selection of the storage engine. I will probably bring up this topic during the `weekly team meeting`_.
* Inspect currently available storage drivers in Marconi - MongoDB_ and SQLAlchemy_. This will give me a better background to start coding the driver for the selected storage engine.
* Write new tests and improve existing tests. Since I don't have much experience working with the testing tools used in Marconi, I would like to gain some insight in this area by performing testing tasks. This way, I would contribute with some tests while making more experience in testing.

Then I will start the implementation following this dependency chain:

* queues > messages > claims
* catalogue > shards

By this time, I expect that most of the driver functionality will be complete.

After that, I would like to spend the last weeks of the internship performing more testing tasks and improving the existing documentation - done in parallel with the implementation -.

It's important to mention that the first three weeks of the internship I will have exams at college and I won't be able to work full time (I estimate 75% of full speed). I will make up for the missing hours by working during weekends. Usually exams at my college are separated by several days, so I will let my mentor know in advance when I will be away and when I will make up those hours.


Select a storage engine (first milestone) (2 weeks)
---------------------------------------------------


Research about existing storage engines (0.5 weeks)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Learn development internals about the current storage engines supported by Marconi.
* Look for storage engines available and make a pre-selection.
* Compare the selected storage engines and analyze which may be the best according to the Marconi goals for the next release.


Discuss with Marconi team members the available possibilities (1 day)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* During the `weekly team meeting`_, request feedback from the Marconi team on the storage engines I had pre-selected.
* Consider their opinions and my personal ideas to select the storage engine to implement.

.. _`weekly team meeting`: https://wiki.openstack.org/wiki/Meetings#Marconi_.28queues.29_team_meeting


Inspect storage drivers currently available in Marconi (2 days)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Check MongoDB_ driver implementation located in `/marconi/queues/storage/mongodb`_.
* Check SQLAlchemy_ driver implementation located in `/marconi/queues/storage/sqlalchemy`_.

.. _`/marconi/queues/storage/mongodb`: https://github.com/openstack/marconi/tree/master/marconi/queues/storage/mongodb
.. _`/marconi/queues/storage/sqlalchemy`: https://github.com/openstack/marconi/tree/master/marconi/queues/storage/sqlalchemy


Get familiar with the testing tools used by Marconi and contribute with some tests (1 week)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Learn about the testing tools used in Marconi.
* Contribute with the creation of additional tests and with tests enhancements. There is a lot to do in this area, e.g. bug 1251740_ and bug 1254158_.

.. _1251740: https://bugs.launchpad.net/marconi/+bug/1251740
.. _1254158 : https://bugs.launchpad.net/marconi/+bug/1254158


Implement the driver for the selected storage engine (second milestone) (6.5 weeks)
-----------------------------------------------------------------------------------

Set up the repository and stub out the driver (0.5 weeks)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Create a new Github project.
* List Marconi as a dependency.
* Stub out the driver implementation. This will include the following files,
  
  + driver.py  - Manages connection with the DB
  + options.py - Storage backend driver configuration options
  + queues.py  - Queues controller
  + messages.py - Messages controller 
  + claims.py - Claims controller
  + catalogue.py - Queues catalogue controller
  + shards.py - Shards management storage controller  


Implement driver connection to storage backend and configuration options (0.5 weeks)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* driver.py

  + connection(conf)
  + is_alive(self)

* options.py

  + _config_options()


Implement queues, messages and claims. Write unit tests and basic documentation (3 weeks)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* queues.py

  + create(self, name, project=None)
  + delete(self, name, project=None) - Delete all messages/claims in queue
  + exists(self, name, project=None)  
  + stats(self, name, project=None)
  + get_metadata(self, name, project=None)
  + set_metadata(self, name, metadata, project=None)
  + list(self, project=None, marker=None, limit=storage.DEFAULT_QUEUES_PER_PAGE, detailed=False)  

* messages.py

  + get(self, queue_name, message_id, project=None)
  + bulk_get(self, queue_name, message_ids, project=None)
  + post(self, queue_name, messages, client_uuid, project=None)
  + delete(self, queue_name, message_id, project=None, claim=None)  
  + bulk_delete(self, queue_name, message_ids, project=None)
  + first(self, queue_name, project=None, sort=1)
  + _claimed(self, queue_name, claim_id, expires=None, limit=None, project=None)
  + _unclaim(self, queue_name, claim_id, project=None)
  + _active(self, queue_name, marker=None, echo=False, client_uuid=None, fields=None, project=None, limit=None)
  + _count(self, queue_name, project=None, include_claimed=False)
  + list(self, queue_name, project=None, marker=None, limit=storage.DEFAULT_MESSAGES_PER_PAGE, echo=False, client_uuid=None, include_claimed=False)~

* claims.py

  + get(self, queue, claim_id, project=None)
  + create(self, queue, metadata, project=None, limit=storage.DEFAULT_MESSAGES_PER_CLAIM)
  + update(self, queue, claim_id, metadata, project=None)
  + delete(self, queue, claim_id, project=None)


Implement catalogue and shards. Write unit tests and basic documentation (2 weeks)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* catalogue.py

  + insert(self, project, queue, shard)
  + delete(self, project, queue)
  + update(self, project, queue, shard=None)
  + get(self, project, queue)
  + exists(self, project, queue)
  + list(self, project)
  + drop_all(self)
  
* shards.py

  + create(self, name, weight, uri, options=None)
  + delete(self, name)
  + update(self, name, \**kwargs)
  + get(self, name, detailed=False)
  + exists(self, name)
  + list(self, marker=None, limit=10, detailed=False)  
  + drop_all(self)


Implement driver support for the added controllers. Write unit tests and basic documentation (0.5 week)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* driver.py

  + queues_database(self)
  + queue_controller(self)
  + message_databases(self)  
  + message_controller(self)
  + claim_controller(self)
  + shards_controller(self)
  + catalogue_controller(self)


Run additional tests and enhance technical documentation (third milestone) (2.5 weeks)
--------------------------------------------------------------------------------------

Run additional tests (1.5 weeks)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Create and run additional tests to assess the nuances of the added backend.
* Reuse currently available `functional tests`_ to run against the added storage engine.

.. _`functional tests`: https://github.com/openstack/marconi/tree/master/marconi/tests/functional


Create an user manual and improve technical documentation in general (1 week)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Create a brief user manual using the documentation added during the implementation stage and all details that could be missing.
* Update and extend, if necessary, the technical documentation added during the implementation stage.


If time permits...
------------------

It would be nice to provide more extensive documentation for the added storage engine. I could include:

* Detailed features provided by the storage engine and a brief comparative with similar solutions
* Benchmarks comparing the added backend with existing backends (e.g. MongoDB)
* Examples demonstrating where the added backend would be more effective

Also, it would be great to create a package and make it available on PyPI.


About me
========

I'm Victoria Martínez de la Cruz, a Licentiate in Computer Sciences student at `Universidad Nacional del Sur`_ in Bahía Blanca, Buenos Aires, Argentina. From January to April 2013 I worked as an `OpenStack intern`_ as part of the `Outreach Program for Women (OPW)`_ .

In college, among other things, I learned about computer architectures, operative system internals, good practices in software development and, of course, several programming languages including Python, Java and C.

During my internship in OpenStack, I was able to apply my knowledge and got some experience working with Python. I also had the chance to learn about tools and practices used in real world software development organizations, which I enjoyed sharing in my personal blog. Some of my most visited posts are `In a nutshell: How OpenStack works`_, `Logging and debugging in OpenStack`_ and `Getting started with Marconi, the message queue for OpenStack`_.

I have been looking forward for start contributing to an open-source organization from many years now - I was 13 years old when I heard about and became interested in the open-source philosophy - and thanks to the OPW I got in touch with the OpenStack community.

Since last year, I have been contributing mainly to OpenStack Dashboard (Horizon) and OpenStack Internationalization.

`The Marconi project caught my attention from its beginning`_ but due to time constraints, mainly because of college duties, I haven't been able to make stronger contributions. I'm really excited to have this opportunity to finally contribute to Marconi with a significant feature and be able to blog about that so new contributors can join our effort in the near future.

For more details about my contributions to OpenStack, you can visit my `personal blog`_ and also check a `list of recent contributions`_ in Gerrit.

You can reach me on IRC at irc.freenode.org in #openstack, #openstack-horizon and #openstack-marconi - my IRC handle is vkmc -, or through my personal email at victoria@vmartinezdelacruz.com.

.. _`Universidad Nacional del Sur`: http://cs.uns.edu.ar/home/
.. _`Outreach Program for Women (OPW)`: https://gnome.org/opw/
.. _`OpenStack intern`: https://wiki.gnome.org/OutreachProgramForWomen/2013/JanuaryApril#Accepted_Participants
.. _`In a nutshell: How OpenStack works`: http://vmartinezdelacruz.com/in-a-nutshell-how-openstack-works/
.. _`Logging and debugging in OpenStack`: http://vmartinezdelacruz.com/logging-and-debugging-in-openstack/
.. _`Getting started with Marconi, the message queue for OpenStack`: http://vmartinezdelacruz.com/getting-started-with-marconi-the-message-queue-for-openstack/ 
.. _`The Marconi project caught my attention from its beginning`: http://vmartinezdelacruz.com/getting-started-with-marconi-the-message-queue-for-openstack/
.. _`personal blog`: http://vmartinezdelacruz.com
.. _`list of recent contributions`: https://review.openstack.org/#/q/owner:victoria,n,z
