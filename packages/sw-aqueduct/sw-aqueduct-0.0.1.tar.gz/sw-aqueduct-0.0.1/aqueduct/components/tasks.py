# Copyright: (c) 2022, Swimlane <info@swimlane.com>
# MIT License (see LICENSE or https://opensource.org/licenses/MIT)

from ..base import Base


class Tasks(Base):

    """Used to sync tasks from a source instance to a destination instance of Swimlane
    """

    def sync_task(self, task):
        """This method syncs a single task from a source Swimlane instance to a destination instance.

        Using the provided task dictionary from Swimlane source instance we first get the actual task
        object from the source.

        Next we also attempt to retrieve the task from the destination system.

        If the task does not exist on the destination then we add it.

        If it does exist, we check if the `uid` and the `version` are the same.
        If they are the same we skip updating the task.

        If they are different then we update the task on the destination instance.

        Args:
            task (dict): A Swimlane task object from a source system.

        Returns:
            dict: If we failed to add a task we return it so we can try again - only if called using the sync method.
        """
        if not self._is_in_include_exclude_lists(task['name'], 'tasks'):
            self.__logger.info(f"Processing task '{task['name']}'.")
            task_ = self.source_instance.get_task(task['id'])
            dest_task = self.destination_instance.get_task(task['id'])
            if not dest_task:
                self.__logger.info(f"Creating task '{task_['name']}' on destination.")
                try:
                    dest_task = self.destination_instance.add_task(task_)
                    self.__logger.info(f"Successfully added task '{task_['name']}' to destination.")
                except:
                    self.__logger.warning(f"Failed to add task '{task_['name']}' to destination.")
                    self.__logger.info(f"Will attempt again before finalizing.")
                    return task_
            else:
                self.__logger.info(f"Task '{task_['name']}' already exists on destination.")
                if task_.get('uid') and dest_task.get('uid') and task_['uid'] == dest_task['uid']:
                    if task_.get('version') and dest_task.get('version') and task_['version'] == dest_task['version']:
                        self.__logger.info(f"Task '{task_['name']}' has not changed on destination. Skipping...")
                    else:
                        self.__logger.info(f"Task '{task_['name']}' has changed. Updating...")
                        self.destination_instance.update_task(dest_task['id'], task_)
                        self.__logger.info(f"Successfully updated task '{task_['name']}' on destination.")

    def sync(self):
        """This method is used to sync all tasks from a source instance to a destination instance
        """
        self.__logger.info(f"Starting to sync tasks from '{self.source_host}' to '{self.dest_host}'")
        failed_task_list = []
        for task in self.source_instance.get_tasks()['tasks']:
            resp = self.sync_task(task=task)
            if resp:
                failed_task_list.append(resp)

        if failed_task_list:
            count = 1
            self.__logger.info("Retrying failed task migration from host to destination.")
            while count < 3:
                for task_ in failed_task_list:
                    self.__logger.info(f"Attempt {count}: Processing task '{task_['name']}'.")
                    self.__logger.info(f"Creating task '{task_['name']}' on destination.")
                    try:
                        dest_task = self.destination_instance.add_task(task_)
                        self.__logger.info(f"Successfully added task '{task_['name']}' to destination.")
                        failed_task_list.pop(task_)
                    except:
                        self.__logger.warning(f"Failed to add task '{task_['name']}' to destination.")
                count += 1
            
            if len(failed_task_list) > 0:
                self.__logger.critical(f"The following task were unable to be added to destination! {[x['name'] for x in failed_task_list]}")
                raise Exception()
