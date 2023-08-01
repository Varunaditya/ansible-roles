# Ansible Role For Configuring Apache Kafka

This Ansible role install and configures Apache Kafka on target systems. By default, the role uses the `KRaft` server mode and assigns the role of `controller` & `broker` to all the nodes.

## Requirements

- Ansible 2.10 or later
- Target system should have python running on a supported operating system

## Role Variables

The following variables can be customized to configure the RabbitMQ server:

- `kafka_mode`: The mode in which Kafka should be deployed. As of now, the role only supports kraft mode. The deafult value is `kraft`.
- `kafka_version`: The version of Kafka. The default value is `3.5.0`.
- `kafka_scala_version`: The verison of Scala to be used with Kafka. The default value is `2.13`.
- `kafka_jmx_version`: The version of JMX exporter. The default valeu is `0.19.0`.
- `kafka_jmx_enable`: Whether to enable JMX exporter or not. The default value is `True`.
- `kraft_production_ready`: To use production ready version of Kafka or not. This needs to be set to False if Kafka verion older than `3.5.0` needs to be used with `KRaft mode`. The deafult is `True`.
- `kafka_group`: The UNIX group that would own the Kafka related data. The default value is `kafka`.
- `kafka_user`: The UNIX user that would own the Kafka related data. The default value is `kafka`.
- `kafka_installation_location`: The path where the Kafka installation will be present. The default value is `/kafka`.
- `kafka_data_dir`: The path where Kafka logs and metadata will be stored. The default value is `{{ kafka_installation_location }}/logs`.
- `kafka_controller_port`: The TCP port the controller will use. The default value is `9093`.
- `kafka_broker_port`: The TCP port the broker will use. The default value is `9092`.
- `log_retention_hours`: The number of hours to keep a log file before deleting it (in hours). The default value is `168`.
- `auto_leader_rebalance_enable`: Enables auto leader balancing. The default value is `True`.
- `auto_create_topics_enable`: Enable auto creation of topic on the server. The default value is `False`.

It is required that the value of the following parameters do not go above the number of brokers.  
If the value of either of the parameters go above the number of brokers, this Ansible role lowers the value to the number of brokers.  
For example, if there are `3` brokers and the value of `offsets_topic_replication_factor` is set to `5`, the final configured value would be `3`.

- `offsets_topic_replication_factor`: The replication factor for the offsets topic. The default value is `3`.
- `transaction_state_log_replication_factor`: The replication factor for the transaction topic. The default value is `2`.
- `transaction_state_log_min_isr`: Overridden min.insync.replicas config for the transaction topic. The default value is `2`.

#### More details about these configuration parameters - [Kafka Broker Configurations](https://kafka.apache.org/documentation/#brokerconfigs)

## Dependencies

This role has no dependencies on other Ansible roles.

## Example Playbook

Here's an example playbook that uses this role:

```yaml
- name: Install and configure Apache Kafka
  hosts: "{{ custom_hosts | default('kafka-server') }}"
  become: true
  roles:
    - kafka
```

## To use this playbook, save it as playbooks/kafka/{purpose}-kafka-{project}-cluster.yml, and then run the following command

ansible-playbook playbooks/kafka/{purpose}-kafka-{project}-cluster.yml

# Maintainers
👤  Core Infra - @Varunaditya (varunaditya.jadwal@tiket.com) 
