// ignore_for_file: no_leading_underscores_for_local_identifiers

import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:font_awesome_flutter/font_awesome_flutter.dart';
import 'package:persistent_bottom_nav_bar/persistent_tab_view.dart';
import 'package:smart_farming/popular_crops.dart';
import 'package:smart_farming/soil_input.dart';

class BottomNavBar extends StatefulWidget {
  const BottomNavBar({super.key});

  @override
  State<BottomNavBar> createState() => _BottomNavBarState();
}

class _BottomNavBarState extends State<BottomNavBar> {
  @override
  Widget build(BuildContext context) {
    List<Widget> _buildScreens() {
      return [
        const SoilInputScreen(),
        const PopularCropsScreen()
      ];
    }

    List<PersistentBottomNavBarItem> _navBarsItems() {
      return [
        PersistentBottomNavBarItem(
          icon: const FaIcon(
            FontAwesomeIcons.earthAfrica,
            size: 22,
          ),
          title: ("Soil Input"),
          textStyle: const TextStyle(fontSize: 12, fontWeight: FontWeight.bold),
          activeColorPrimary: Theme.of(context).colorScheme.secondary,
          inactiveColorPrimary: Colors.black38,
        ),
        PersistentBottomNavBarItem(
          icon: const Center(
            child: FaIcon(
              FontAwesomeIcons.star,
              size: 22,
            ),
          ),
          title: ("Rating & Review"),
          textStyle: const TextStyle(fontSize: 12, fontWeight: FontWeight.bold),
          activeColorPrimary: Theme.of(context).colorScheme.secondary,
          inactiveColorPrimary: Colors.black38,
        ),
      ];
    }

    PersistentTabController controller;

    controller = PersistentTabController(initialIndex: 0);

    return WillPopScope(
      onWillPop: () async {
        return await showDialog(
            barrierDismissible: false,
            context: context,
            builder: (BuildContext context) {
              return AlertDialog(
                title: const Text(
                  'Are you sure you want to exit?',
                  textAlign: TextAlign.center,
                ),
                actions: [
                  TextButton(
                    onPressed: () {
                      Navigator.of(context).pop();
                    },
                    child: const Text('No',
                        style: TextStyle(color: Colors.black, fontSize: 20)),
                  ),
                  TextButton(
                    onPressed: () {
                      SystemNavigator.pop();
                    },
                    child: const Text('Yes',
                        style: TextStyle(color: Colors.red, fontSize: 20)),
                  ),
                ],
              );
            });
      },
      child: PersistentTabView(
        context,
        controller: controller,
        screens: _buildScreens(),
        items: _navBarsItems(),
        // hideNavigationBar: ref.watch(hideNavBarProvider)==true?true:false,
        confineInSafeArea: true,
        backgroundColor: Colors.white, // Default is Colors.white.
        handleAndroidBackButtonPress: true, // Default is true.
        resizeToAvoidBottomInset:
            true, // This needs to be true if you want to move up the screen when keyboard appears. Default is true.
        stateManagement: true, // Default is true.
        hideNavigationBarWhenKeyboardShows:
            true, // Recommended to set 'resizeToAvoidBottomInset' as true while using this argument. Default is true.
        decoration: NavBarDecoration(
          borderRadius: BorderRadius.circular(10.0),
          colorBehindNavBar:
              const Color.fromARGB(255, 236, 228, 228).withOpacity(0.3),
        ),
        popAllScreensOnTapOfSelectedTab: true,
        popActionScreens: PopActionScreensType.all,
        itemAnimationProperties: const ItemAnimationProperties(
          // Navigation Bar's items animation properties.
          duration: Duration(milliseconds: 400),
          curve: Curves.ease,
        ),
        screenTransitionAnimation: const ScreenTransitionAnimation(
          // Screen transition animation on change of selected tab.
          animateTabTransition: true,
          curve: Curves.ease,
          duration: Duration(milliseconds: 400),
        ),
        navBarStyle:
            NavBarStyle.style9, // Choose the nav bar style with this property.
      ),
    );
  }
}