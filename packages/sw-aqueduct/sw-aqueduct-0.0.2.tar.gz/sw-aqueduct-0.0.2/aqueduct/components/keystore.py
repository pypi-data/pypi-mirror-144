# Copyright: (c) 2022, Swimlane <info@swimlane.com>
# MIT License (see LICENSE or https://opensource.org/licenses/MIT)

from ..base import Base


class KeyStore(Base):

    """Used to sync keystore items from a source instance to a destination instance of Swimlane
    """

    def sync(self):
        """Syncing of the keystore will only create new entries into the destination systems keystore.
    The creation of these items does not transfer or implement the transfer of the value since
    these are encrypted within Swimlane themselves.

    Once items are created in the keystore on the destination system then you must manually enter 
    the value for that keystore item.
    """
        self.__logger.info(f"Attempting to sync keystore from '{self.source_host}' to '{self.dest_host}'")
        credentials = self.source_instance.get_credentials()
        credentials.pop('$type')
        for key,val in credentials.items():
            if not self._is_in_include_exclude_lists(key, 'keystore'):
                self.__logger.info(f"Processing '{key}' credential")
                if not self.destination_instance.get_credential(key):
                    self.__logger.info(f"Adding Keystore item '{key}' to destination.")
                    credential_ = self.source_instance.get_credential(key)
                    self.destination_instance.add_credential(credential_)
                    self.__logger.info(f"Successfully added new keystore item '{key}'")
                else:
                    self.__logger.info(f"Keystore item '{key}' exists on destination. Skipping....")
