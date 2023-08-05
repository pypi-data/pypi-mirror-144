# Copyright: (c) 2022, Swimlane <info@swimlane.com>
# MIT License (see LICENSE or https://opensource.org/licenses/MIT)

from ..base import Base
from .reports import Reports
from ..models import Dashboard


class Dashboards(Base):

    """Used to sync dashboards from a source instance to a destination instance of Swimlane
    """

    def __process_reports(self, dashboard: Dashboard, force=False):
        self.__logger.info(f"Processing dashboard '{dashboard.name}' reports.")
        for item in dashboard.items:
            report = self.source_instance.get_report(report_id=item.reportId)
            Reports().sync_report(report=report, force=force)

    def __get_dashboard_items(self, source: Dashboard, destination: Dashboard):
        self.__logger.info(f"Comparing dashboard items from source and destination")
        return_list = []
        for item in source.items:
            if item not in destination.items:
                return_list.append(item)
        return return_list

    def sync_dashboard(self, dashboard: Dashboard):
        """This method syncs a single dashboard from a source instance to a destination instance.

        This class first checks to see if the provided dashboard already exists on the destination instance.
        If it does not exist then we attempt to add the dashboard to the destination instance.

        If it already exists on the destination instance we first check it against all destination
        instance dashboards. This check involves comparing the provided source dashboard dict with 
        the `uid` and `name` of a destination instance dashboard.

        If a match is found we then check if the version is the same. If it is we simply skip processing this dashboard.

        If a match is found but the versions are different we first ensure that all the reports in the dashboard are on 
        the destination instance. Once that is complete we modify the dashboard to remove unneeded keys and then update it
        as provided by the source instance.

        Args:
            dashboard (dict): A source instance dashboard dictionary.
        """
        if not self._is_in_include_exclude_lists(dashboard.name, 'dashboards'):
            self.__logger.info(f"Processing dashboard '{dashboard.name}' ({dashboard.id})")
            dest_dashboard = self.destination_instance.dashboard_dict.get(dashboard.uid)
            if not dest_dashboard:
                self.__process_reports(dashboard=dashboard, force=True)
                self.__logger.info(f"Adding dashboard '{dashboard.name}' for workspaces '{dashboard.workspaces}' on destination")
                resp = self.destination_instance.add_dashboard(dashboard)
                self.__logger.info(f"Successfully added dashboard '{dashboard.name}' to destination.")
            else:
                if self.update_dashboards:
                    self.__logger.info(f"Dashboard '{dashboard.name}' for workspaces '{dashboard.workspaces}' was found. Making sure all reports exist...")
                    self.__process_reports(dashboard=dashboard, force=True)
                    self.__logger.info(f"Updating '{dashboard.name}' now.")
                    dest_dashboard.items = self.__get_dashboard_items(dashboard, dest_dashboard)
                    self.destination_instance.update_dashboard(dest_dashboard)
                    self.__logger.info(f"Successfully updated dashboard '{dashboard.name}'.")
                else:
                    self.__logger.info(f"Skipping check of dashboard '{dashboard.name}' for changes since update_dashboards is False.")

    def sync(self):
        """This method is used to sync all dashboards from a source instance to a destination instance
        """
        self.__logger.info(f"Attempting to sync dashboards from '{self.source_host}' to '{self.dest_host}'")
        for id, dashboard in self.source_instance.dashboard_dict.items():
            self.sync_dashboard(dashboard=dashboard)
