# Installation Guide for custom_pc_odoo_17_v4

This guide provides step-by-step instructions for installing the `custom_pc_odoo_17_v4` module on Odoo 17 Community Edition.

## Prerequisites

- Odoo 17 Community Edition installed on your system.
- Access to the Odoo server (local or remote).
- Basic knowledge of using the command line.

## Installation Steps

1. Download the `custom_pc_odoo_17_v4` module from the repository.

2. Copy the `custom_pc_odoo_17_v4` folder into the Odoo addons directory. The typical path is `/odoo/odoo-server/addons/`.

3. Restart the Odoo server. If you're running Odoo from the command line, you can stop the server using `Ctrl+C` and start it again using the command you used before (typically `./odoo-bin`).

4. Update the modules list in Odoo. You can do this by navigating to the `Apps` menu, removing the 'Apps' filter in the search bar, and clicking on 'Update Apps List'.

5. Search for `custom_pc_odoo_17_v4` in the Apps menu. You should see the module in the list.

6. Click on `Install` to install the module.

## Post-Installation Steps

After the module is installed, you should see new menus in the Odoo interface related to PC building. If you can't see the new menus, please refresh the page.

If you encounter any issues during the installation, please refer to the `developer_guide.md` for more information about the module structure and code.

Congratulations, you have successfully installed the `custom_pc_odoo_17_v4` module! You can now start customizing PCs in your Odoo interface. For more information on how to use the module, please refer to the `user_guide.md`.