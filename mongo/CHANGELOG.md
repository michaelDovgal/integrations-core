# CHANGELOG - mongo

## 4.0.0 / 2022-08-05

* [Added] Support allow invalid hostnames in SSL connections. See [#12541](https://github.com/DataDog/integrations-core/pull/12541).
* [Added] Added new metrics for oplatencies. See [#12479](https://github.com/DataDog/integrations-core/pull/12479).
* [Added] Added new metric "mongodb.metrics.queryexecutor.scannedobjectsps". See [#12467](https://github.com/DataDog/integrations-core/pull/12467).
* [Added] Add dbnames allowlist config option. See [#12450](https://github.com/DataDog/integrations-core/pull/12450).
* [Added] Ship `pymongo-srv` to support DNS seed connection schemas. See [#12442](https://github.com/DataDog/integrations-core/pull/12442).
* [Fixed] Dependency updates. See [#12653](https://github.com/DataDog/integrations-core/pull/12653).
* [Changed] Upgrade pymongo to 4.2. See [#12594](https://github.com/DataDog/integrations-core/pull/12594).

## 3.2.3 / 2022-06-27 / Agent 7.38.0

* [Fixed] Allow hosts to be a singular value. See [#12090](https://github.com/DataDog/integrations-core/pull/12090).

## 3.2.2 / 2022-05-15 / Agent 7.37.0

* [Fixed] Capture badly formatted hosts. See [#11933](https://github.com/DataDog/integrations-core/pull/11933).

## 3.2.1 / 2022-04-26

* [Fixed] Fix passing in username and password as options. See [#11525](https://github.com/DataDog/integrations-core/pull/11525).

## 3.2.0 / 2022-04-05 / Agent 7.36.0

* [Added] Upgrade dependencies. See [#11726](https://github.com/DataDog/integrations-core/pull/11726).
* [Added] Add metric_patterns options to filter all metric submission by a list of regexes. See [#11695](https://github.com/DataDog/integrations-core/pull/11695).
* [Fixed] Support newer versions of `click`. See [#11746](https://github.com/DataDog/integrations-core/pull/11746).

## 3.1.0 / 2022-02-19 / Agent 7.35.0

* [Added] Add `pyproject.toml` file. See [#11399](https://github.com/DataDog/integrations-core/pull/11399).
* [Fixed] Fix namespace packaging on Python 2. See [#11532](https://github.com/DataDog/integrations-core/pull/11532).
* [Fixed] Small code nits. See [#11127](https://github.com/DataDog/integrations-core/pull/11127).

## 3.0.0 / 2022-01-08 / Agent 7.34.0

* [Fixed] Don't add autogenerated comments to deprecation files. See [#11014](https://github.com/DataDog/integrations-core/pull/11014).
* [Fixed] Add comment to autogenerated model files. See [#10945](https://github.com/DataDog/integrations-core/pull/10945).
* [Fixed] Refresh role on replica sets and add more debug logging. See [#10843](https://github.com/DataDog/integrations-core/pull/10843).
* [Changed] Add `server` default group for all monitor special cases. See [#10976](https://github.com/DataDog/integrations-core/pull/10976).

## 2.7.1 / 2021-10-25 / Agent 7.33.0

* [Fixed] Load CA certs if SSL is enabled and CA certs are not passed in the configurations. See [#10377](https://github.com/DataDog/integrations-core/pull/10377).

## 2.7.0 / 2021-10-04 / Agent 7.32.0

* [Added] Disable generic tags. See [#10027](https://github.com/DataDog/integrations-core/pull/10027).
* [Added] Add runtime configuration validation. See [#8957](https://github.com/DataDog/integrations-core/pull/8957).

## 2.6.0 / 2021-08-22 / Agent 7.31.0

* [Added] Support collection-agnostic aggregations for custom queries. See [#9857](https://github.com/DataDog/integrations-core/pull/9857).

## 2.5.0 / 2021-07-12 / Agent 7.30.0

* [Added] Bump pymongo to 3.8. See [#9557](https://github.com/DataDog/integrations-core/pull/9557).
* [Fixed] Update description of the `hosts` config parameter. See [#9542](https://github.com/DataDog/integrations-core/pull/9542).

## 2.4.0 / 2021-04-19 / Agent 7.28.0

* [Fixed] Fix authSource config option.. See [#9139](https://github.com/DataDog/integrations-core/pull/9139).
* [Deprecated] Deprecate connection_scheme. See [#9142](https://github.com/DataDog/integrations-core/pull/9142).

## 2.3.1 / 2021-04-06

* [Fixed] Fix no_auth support. See [#9094](https://github.com/DataDog/integrations-core/pull/9094).

## 2.3.0 / 2021-03-11 / Agent 7.27.0

* [Added] Cache API client connection. See [#8808](https://github.com/DataDog/integrations-core/pull/8808).

## 2.2.1 / 2021-03-07

* [Fixed] Support Alibaba ApsaraDB. See [#8316](https://github.com/DataDog/integrations-core/pull/8316).
* [Fixed] Rename config spec example consumer option `default` to `display_default`. See [#8593](https://github.com/DataDog/integrations-core/pull/8593).
* [Fixed] Bump minimum base package version. See [#8443](https://github.com/DataDog/integrations-core/pull/8443).

## 2.2.0 / 2021-01-25 / Agent 7.26.0

* [Added] Better arbiter support. See [#8294](https://github.com/DataDog/integrations-core/pull/8294).
* [Fixed] Refactor connection and api. See [#8283](https://github.com/DataDog/integrations-core/pull/8283).

## 2.1.1 / 2020-12-11 / Agent 7.25.0

* [Fixed] Log custom queries which return an empty result set. See [#8105](https://github.com/DataDog/integrations-core/pull/8105).

## 2.1.0 / 2020-11-10 / Agent 7.24.0

* [Added] Add mongodb.connection_pool.totalinuse. See [#7986](https://github.com/DataDog/integrations-core/pull/7986).
* [Fixed] Ignore startup nodes for lagtime. See [#7990](https://github.com/DataDog/integrations-core/pull/7990).

## 2.0.3 / 2020-11-09

* [Fixed] Fix debug typo for custom queries. See [#7969](https://github.com/DataDog/integrations-core/pull/7969).

## 2.0.2 / 2020-11-06

* [Fixed] Fix replicaset identification with old configuration. See [#7964](https://github.com/DataDog/integrations-core/pull/7964).

## 2.0.1 / 2020-11-06

* [Fixed] Add sharding_cluster_role tag to optime_lag metric. See [#7956](https://github.com/DataDog/integrations-core/pull/7956).

## 2.0.0 / 2020-10-31

* [Added] New replication lag metric collected from the primary. See [#7828](https://github.com/DataDog/integrations-core/pull/7828).
* [Added] Add the shard cluster role as a tag. See [#7834](https://github.com/DataDog/integrations-core/pull/7834).
* [Added] Add new metrics for mongos. See [#7770](https://github.com/DataDog/integrations-core/pull/7770).
* [Added] Allow specifying a different database in custom queries. See [#7808](https://github.com/DataDog/integrations-core/pull/7808).
* [Added] [doc] Add encoding in log config sample. See [#7708](https://github.com/DataDog/integrations-core/pull/7708).
* [Fixed] Fix warning when adding 'jumbo_chunks' metrics. See [#7833](https://github.com/DataDog/integrations-core/pull/7833).
* [Fixed] Fix building of the connection string. See [#7744](https://github.com/DataDog/integrations-core/pull/7744).
* [Fixed] Refactor collection logic. See [#7615](https://github.com/DataDog/integrations-core/pull/7615).
* [Changed] Stop collecting custom queries from secondaries by default. See [#7794](https://github.com/DataDog/integrations-core/pull/7794).
* [Changed] Collect only the metrics that make sense based on the type of mongo instance. See [#7713](https://github.com/DataDog/integrations-core/pull/7713).

## 1.16.5 / 2020-09-21 / Agent 7.23.0

* [Fixed] Submit collection metrics even if value is zero. See [#7606](https://github.com/DataDog/integrations-core/pull/7606).
* [Fixed] Fix style for the latest release of Black. See [#7438](https://github.com/DataDog/integrations-core/pull/7438).

## 1.16.4 / 2020-08-19

* [Fixed] Avoid depleting collection_metric_names. See [#7393](https://github.com/DataDog/integrations-core/pull/7393).

## 1.16.3 / 2020-08-10 / Agent 7.22.0

* [Fixed] Update logs config service field to optional. See [#7209](https://github.com/DataDog/integrations-core/pull/7209).

## 1.16.2 / 2020-06-29 / Agent 7.21.0

* [Fixed] Fix template specs typos. See [#6912](https://github.com/DataDog/integrations-core/pull/6912).
* [Fixed] Raise an error if only one of `username` or `password` is set. See [#6688](https://github.com/DataDog/integrations-core/pull/6688).

## 1.16.1 / 2020-05-19 / Agent 7.20.0

* [Fixed] Fix encoding and parsing issues when processing connection configuration. See [#6686](https://github.com/DataDog/integrations-core/pull/6686).

## 1.16.0 / 2020-05-17

* [Added] Allow optional dependency installation for all checks. See [#6589](https://github.com/DataDog/integrations-core/pull/6589).

## 1.15.0 / 2020-05-05

* [Deprecated] Refactor connection configuration. See [#6574](https://github.com/DataDog/integrations-core/pull/6574).

## 1.14.0 / 2020-04-04 / Agent 7.19.0

* [Added] Add config specs. See [#6145](https://github.com/DataDog/integrations-core/pull/6145).
* [Fixed] Use new agent signature. See [#6085](https://github.com/DataDog/integrations-core/pull/6085).
* [Fixed] Remove logs sourcecategory. See [#6121](https://github.com/DataDog/integrations-core/pull/6121).
* [Fixed] Replace deprecated method `database_names` by `list_database_names`. See [#5864](https://github.com/DataDog/integrations-core/pull/5864).

## 1.13.0 / 2020-01-13 / Agent 7.17.0

* [Added] Use lazy logging format. See [#5377](https://github.com/DataDog/integrations-core/pull/5377).

## 1.12.0 / 2019-10-11 / Agent 6.15.0

* [Added] Submit version metadata. See [#4722](https://github.com/DataDog/integrations-core/pull/4722).

## 1.11.0 / 2019-07-13 / Agent 6.13.0

* [Added] Upgrade pymongo to 3.8. See [#4095](https://github.com/DataDog/integrations-core/pull/4095).

## 1.10.3 / 2019-06-18

* [Fixed] Reduce doc in configuration file in favor of official documentation. See [#3892](https://github.com/DataDog/integrations-core/pull/3892).

## 1.10.2 / 2019-06-06 / Agent 6.12.0

* [Fixed] Custom queries: add examples and fix logging. See [#3871](https://github.com/DataDog/integrations-core/pull/3871).

## 1.10.1 / 2019-06-05

* [Fixed] Add missing metrics. See [#3856](https://github.com/DataDog/integrations-core/pull/3856).
* [Fixed] Fix 'custom_queries' field name. See [#3868](https://github.com/DataDog/integrations-core/pull/3868).

## 1.10.0 / 2019-06-01

* [Added] Add custom query capabilities. See [#3796](https://github.com/DataDog/integrations-core/pull/3796).

## 1.9.0 / 2019-05-14

* [Added] Add tcmalloc.spinlock_total_delay_ns to mongodb stats. See [#3643](https://github.com/DataDog/integrations-core/pull/3643). Thanks [glenjamin](https://github.com/glenjamin).
* [Added] Adhere to code style. See [#3540](https://github.com/DataDog/integrations-core/pull/3540).

## 1.8.0 / 2019-02-18 / Agent 6.10.0

* [Added] Finish Support Python 3. See [#2916](https://github.com/DataDog/integrations-core/pull/2916).
* [Fixed] Only run `top` against the admin database. See [#2937](https://github.com/DataDog/integrations-core/pull/2937).
* [Added] Support unicode for Python 3 bindings. See [#2869](https://github.com/DataDog/integrations-core/pull/2869).

## 1.7.0 / 2018-11-30 / Agent 6.8.0

* [Added] Support Python 3. See [#2623](https://github.com/DataDog/integrations-core/pull/2623).
* [Fixed] Use raw string literals when \ is present. See [#2465](https://github.com/DataDog/integrations-core/pull/2465).

## 1.6.1 / 2018-09-04 / Agent 6.5.0

* [Fixed] Add data files to the wheel package. See [#1727](https://github.com/DataDog/integrations-core/pull/1727).

## 1.6.0 / 2018-06-13 / Agent 6.4.0

* [Added] [mongo] allow disabling of replica access. See [#1516](https://github.com/DataDog/integrations-core/pull/1516).
* [Changed] [mongo] properly parse metric. See [#1498](https://github.com/DataDog/integrations-core/pull/1498).

## 1.5.4 / Unreleased

* [IMPROVEMENT] Allow disabling of replica access. See #1516

## 1.5.3 / 2018-05-11

* [BUGFIX] Added `top` metrics ending in `countps` that properly submit as `rate`s. See #1491

## 1.5.2 / 2018-02-13

* [DOC] Adding configuration for log collection in `conf.yaml`
* [BUGFIX] Pass replica set metric collection if `replSetGetStatus` command not available. See [#1092](https://github.com/DataDog/integrations-core/issues/1092)

## 1.5.1 / 2018-01-10

* [BUGFIX] Pass replica set metric collection if not running standalone instance instead of raising exception. See [#915](https://github.com/DataDog/integrations-core/issues/915)

## 1.5.0 / 2017-11-21

* [FEATURE] Collect metrics about indexes usage. See [#823](https://github.com/DataDog/integrations-core/issues/823)
* [IMPROVEMENT] Upgrading pymongo to version 3.5. See [#747](https://github.com/DataDog/integrations-core/issues/747)
* [IMPROVEMENT] Filter out oplog entries without a timestamp. See [#406](https://github.com/DataDog/integrations-core/issues/406), thanks [@hindmanj](https://github.com/hindmanj)

## 1.4.0 / 2017-10-10

* [IMPROVEMENT] Started monitoring the wiredTiger cache page read/write statistics. See [#769](https://github.com/DataDog/integrations-core/issues/769) (Thanks [@dnavre](https://github.com/dnavre))

## 1.3.0 / 2017-08-28

* [FEATURE] Add support for `authSource` parameter in mongo URL. See [#691](https://github.com/DataDog/integrations-core/issues/691)
* [IMPROVEMENT] Simplify "system.namespaces" usage. See [#625](https://github.com/DataDog/integrations-core/issues/625), thanks [@dtbartle](https://github.com/dtbartle)
* [BUGFIX] Don't overwrite the higher-level `cli`/`db` for replset stats. See [#627](https://github.com/DataDog/integrations-core/issues/627), thanks [@dtbartle](https://github.com/dtbartle)

## 1.2.0 / 2017-07-18

* [IMPROVEMENT] Add support for `mongo.oplog.*` metrics for Mongo versions  3.x. See [#491](https://github.com/DataDog/integrations-core/issues/491)

## 1.1.0 / 2017-06-05

* [IMPROVEMENT] Set connectTimeout & serverSelectionTimeout to timeout in config. See [#352](https://github.com/DataDog/integrations-core/issues/352)

## 1.0.1 / 2017-04-24

* [BUGFIX] Redact username/password in logs, etc. See [#326](https://github.com/DataDog/integrations-core/issues/326) and [#347](https://github.com/DataDog/integrations-core/issues/347)

## 1.0.0 / 2017-03-22

* [FEATURE] adds mongo integration.