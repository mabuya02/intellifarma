import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:persistent_bottom_nav_bar/persistent_tab_view.dart';
import 'package:smart_farming/login.dart';
import 'package:smart_farming/recommendation.dart';
import 'package:smart_farming/screen_constants.dart';
import 'package:smart_farming/textfield_widget.dart';

class SoilInputScreen extends StatefulWidget {
  const SoilInputScreen({super.key});

  @override
  State<SoilInputScreen> createState() => _SoilInputScreenState();
}

class _SoilInputScreenState extends State<SoilInputScreen> {
  final _soilInputFormKey = GlobalKey<FormState>();
  bool isLoading = false;
  final TextEditingController nitrogenLevelController = TextEditingController();
  final TextEditingController phosphorousLevelController =
      TextEditingController();
  final TextEditingController potassiumLevelController =
      TextEditingController();
  final TextEditingController temperatureController = TextEditingController();
  final TextEditingController humidityController = TextEditingController();
  final TextEditingController pHLevelController = TextEditingController();
  final TextEditingController rainfallController = TextEditingController();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: PreferredSize(
        preferredSize: const Size.fromHeight(40.0),
        child: AppBar(
          backgroundColor: Theme.of(context).colorScheme.background,
          elevation: 0.0,
          actions: [
            IconButton(
              onPressed: () {
                PersistentNavBarNavigator.pushNewScreen(
                  context,
                  screen: const LoginScreen(),
                  withNavBar: false, // OPTIONAL VALUE. True by default.
                  pageTransitionAnimation: PageTransitionAnimation.cupertino,
                );
              },
              icon: const Icon(
                Icons.logout,
                color: Colors.red,
                size: 30.0,
              ),
            ),
          ],
        ),
      ),
      body: Padding(
        padding: const EdgeInsets.all(20),
        child: ListView(
          children: [
            Column(
              crossAxisAlignment: CrossAxisAlignment.center,
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                Container(
                  height: isMediumMobile(context) ? 100 : 120,
                  width: isMediumMobile(context) ? 100 : 120,
                  decoration: BoxDecoration(
                    borderRadius: BorderRadius.circular(20.0),
                    border: Border.all(
                      color: Theme.of(context).colorScheme.primary,
                      width: 2.0,
                    ),
                  ),
                  child: ClipRRect(
                    borderRadius: BorderRadius.circular(20.0),
                    child: Image.asset(
                      'assets/images/logo.png',
                      fit: BoxFit.cover,
                    ),
                  ),
                ),
                const SizedBox(
                  height: 10.0,
                ),
                Text(
                  'Smart Farming',
                  style: TextStyle(
                    fontWeight: FontWeight.w500,
                    fontSize: 25,
                    color: Theme.of(context).colorScheme.primary,
                  ),
                ),
              ],
            ),
            const SizedBox(
              height: 20.0,
            ),
            Form(
              key: _soilInputFormKey,
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  const Text(
                    'Enter your soil parameters:',
                    style: TextStyle(
                      fontWeight: FontWeight.w400,
                      fontSize: 20,
                    ),
                  ),
                  const SizedBox(
                    height: 10,
                  ),
                  CustomTextField(
                    controller: nitrogenLevelController,
                    textInputAction: TextInputAction.next,
                    keyboardType: TextInputType.number,
                    inputFormatters: [
                      FilteringTextInputFormatter.digitsOnly
                    ],
                    validator: (value) {
                      if (value == null || value.isEmpty) {
                        return 'Please provide a valid nitrogen level';
                      } else {
                        return null;
                      }
                    },
                    hintText: 'Nitrogen Level (N)',
                    prefixIcon: const Icon(
                      Icons.grass,
                      size: 20.0,
                    ),
                  ),
                  const SizedBox(
                    height: 20,
                  ),
                  CustomTextField(
                    controller: phosphorousLevelController,
                    textInputAction: TextInputAction.next,
                    keyboardType: TextInputType.number,
                    inputFormatters: [
                      FilteringTextInputFormatter.digitsOnly
                    ],
                    validator: (value) {
                      if (value == null || value.isEmpty) {
                        return 'Please provide a valid phosphorous level';
                      } else {
                        return null;
                      }
                    },
                    hintText: 'Phosphorous Level (P)',
                    prefixIcon: const Icon(
                      Icons.local_florist,
                      size: 20.0,
                    ),
                  ),
                  const SizedBox(
                    height: 20,
                  ),
                  CustomTextField(
                    controller: potassiumLevelController,
                    textInputAction: TextInputAction.next,
                    keyboardType: TextInputType.number,
                    inputFormatters: [
                      FilteringTextInputFormatter.digitsOnly
                    ],
                    validator: (value) {
                      if (value == null || value.isEmpty) {
                        return 'Please provide a valid potassium level';
                      } else {
                        return null;
                      }
                    },
                    hintText: 'Potassium Level (K)',
                    prefixIcon: const Icon(
                      Icons.spa,
                      size: 20.0,
                    ),
                  ),
                  const SizedBox(
                    height: 20.0,
                  ),
                  CustomTextField(
                    controller: temperatureController,
                    textInputAction: TextInputAction.next,
                    keyboardType: TextInputType.number,
                    inputFormatters: [
                      FilteringTextInputFormatter.digitsOnly
                    ],
                    validator: (value) {
                      if (value == null || value.isEmpty) {
                        return 'Please provide a valid temperature';
                      } else {
                        return null;
                      }
                    },
                    hintText: 'Temperature (°C)',
                    prefixIcon: const Icon(
                      Icons.thermostat,
                      size: 20.0,
                    ),
                  ),
                  const SizedBox(
                    height: 20.0,
                  ),
                  CustomTextField(
                    controller: humidityController,
                    textInputAction: TextInputAction.next,
                    keyboardType: TextInputType.number,
                    inputFormatters: [
                      FilteringTextInputFormatter.digitsOnly
                    ],
                    validator: (value) {
                      if (value == null || value.isEmpty) {
                        return 'Please provide a valid humidity';
                      } else {
                        return null;
                      }
                    },
                    hintText: 'Humidity (relative humidity in %)',
                    prefixIcon: const Icon(
                      Icons.opacity,
                      size: 20.0,
                    ),
                  ),
                  const SizedBox(
                    height: 20.0,
                  ),
                  CustomTextField(
                    controller: pHLevelController,
                    textInputAction: TextInputAction.next,
                    keyboardType: TextInputType.number,
                    inputFormatters: [
                      FilteringTextInputFormatter.digitsOnly
                    ],
                    validator: (value) {
                      if (value == null || value.isEmpty) {
                        return 'Please provide a valid pH level';
                      } else {
                        return null;
                      }
                    },
                    hintText: 'pH Level',
                    prefixIcon: const Icon(
                      Icons.whatshot,
                      size: 20.0,
                    ),
                  ),
                  const SizedBox(
                    height: 20.0,
                  ),
                  CustomTextField(
                    controller: rainfallController,
                    textInputAction: TextInputAction.done,
                    keyboardType: TextInputType.number,
                    inputFormatters: [
                      FilteringTextInputFormatter.digitsOnly
                    ],
                    validator: (value) {
                      if (value == null || value.isEmpty) {
                        return 'Please provide a valid rainfall';
                      } else {
                        return null;
                      }
                    },
                    hintText: 'Rainfall (mm)',
                    prefixIcon: const Icon(
                      Icons.beach_access,
                      size: 20.0,
                    ),
                  ),
                  const SizedBox(
                    height: 38.0,
                  ),
                  Center(
                    child: InkWell(
                      onTap: () {
                        if (_soilInputFormKey.currentState!.validate()) {
                          setState(() {
                            isLoading = true;
                          });
                          Future.delayed(const Duration(seconds: 2), () {
                            setState(() {
                              isLoading = false;
                            });
                            PersistentNavBarNavigator.pushNewScreen(
                              context,
                              screen: const RecommendationScreen(),
                              withNavBar:
                                  false, // OPTIONAL VALUE. True by default.
                              pageTransitionAnimation:
                                  PageTransitionAnimation.cupertino,
                            );
                          });
                        }
                      },
                      child: Container(
                        height:isMediumMobile(context) ? 55 : 60,
                        decoration: BoxDecoration(
                          color: Theme.of(context).colorScheme.secondary,
                          border: Border.all(
                            color: Theme.of(context).colorScheme.secondary,
                          ),
                          borderRadius: BorderRadius.circular(15.0),
                        ),
                        child: Center(
                          child: isLoading
                              ? const SizedBox(
                                  height: 30.0,
                                  width: 30.0,
                                  child: CircularProgressIndicator(
                                    color: Colors.white,
                                  ),
                                )
                              : Text(
                                  'Recommend Best Crop',
                                  style: TextStyle(
                                    fontSize: isMediumMobile(context) ? 18 : 20,
                                    fontWeight: FontWeight.bold,
                                    color: Colors.white,
                                  ),
                                ),
                        ),
                      ),
                    ),
                  ),
                  const SizedBox(
                    height: 10.0,
                  ),
                ],
              ),
            ),
          ],
        ),
      ),
    );
  }
}
