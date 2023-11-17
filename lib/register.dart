import 'package:flutter/material.dart';
import 'package:smart_farming/login.dart';
import 'package:smart_farming/screen_constants.dart';
import 'package:smart_farming/textfield_widget.dart';

class RegistrationScreen extends StatefulWidget {
  const RegistrationScreen({super.key});

  @override
  State<RegistrationScreen> createState() => _RegistrationScreenState();
}

class _RegistrationScreenState extends State<RegistrationScreen> {
  final _registerFormKey = GlobalKey<FormState>();
  bool isLoading = false;
  bool isHidden = true;
  bool isHidden2 = true;
  final TextEditingController emailController = TextEditingController();
  final TextEditingController passwordController = TextEditingController();
  final TextEditingController firstNameController = TextEditingController();
  final TextEditingController lastNameController = TextEditingController();
  final TextEditingController reenterPasswordController =
      TextEditingController();
  final TextEditingController phoneNumberController = TextEditingController();
  final TextEditingController farmLocationController = TextEditingController();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: PreferredSize(
        preferredSize: const Size.fromHeight(30.0),
        child: AppBar(
          backgroundColor: Theme.of(context).colorScheme.background,
          elevation: 0.0,
          leading: IconButton(
            onPressed: () {
              Navigator.pushReplacement(
                context,
                MaterialPageRoute(
                  builder: (_) => const LoginScreen(),
                ),
              );
            },
            icon: const Icon(
              Icons.arrow_back,
              color: Colors.black,
            ),
          ),
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
              height: 30.0,
            ),
            Form(
              key: _registerFormKey,
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  const Text(
                    'Register',
                    style: TextStyle(
                      fontWeight: FontWeight.bold,
                      fontSize: 30,
                    ),
                  ),
                  const SizedBox(
                    height: 20,
                  ),
                  CustomTextField(
                    controller: firstNameController,
                    textInputAction: TextInputAction.next,
                    keyboardType: TextInputType.text,
                    validator: (value) {
                      if (value == null || value.isNotEmpty) {
                        return 'Please provide a valid first name';
                      } else {
                        return null;
                      }
                    },
                    hintText: 'First Name',
                    prefixIcon: const Icon(
                      Icons.person,
                      size: 20.0,
                    ),
                  ),
                  const SizedBox(
                    height: 20,
                  ),
                  CustomTextField(
                    controller: lastNameController,
                    textInputAction: TextInputAction.next,
                    keyboardType: TextInputType.text,
                    validator: (value) {
                      if (value == null || value.isNotEmpty) {
                        return 'Please provide a valid last name';
                      } else {
                        return null;
                      }
                    },
                    hintText: 'Last Name',
                    prefixIcon: const Icon(
                      Icons.person,
                      size: 20.0,
                    ),
                  ),
                  const SizedBox(
                    height: 20,
                  ),
                  CustomTextField(
                    controller: emailController,
                    textInputAction: TextInputAction.next,
                    keyboardType: TextInputType.emailAddress,
                    validator: (value) {
                      if (value == null || !value.contains('@')) {
                        return 'Please provide a valid email address';
                      } else {
                        return null;
                      }
                    },
                    hintText: 'Email',
                    prefixIcon: const Icon(
                      Icons.email_rounded,
                      size: 20.0,
                    ),
                  ),
                  const SizedBox(
                    height: 20.0,
                  ),
                  TextFormField(
                    controller: passwordController,
                    textInputAction: TextInputAction.next,
                    keyboardType: TextInputType.text,
                    validator: (value) {
                      if (value == null || value.length < 6) {
                        return 'Please provide a password more than 6 characters';
                      } else {
                        return null;
                      }
                    },
                    obscureText: isHidden,
                    enableSuggestions: false,
                    autocorrect: false,
                    decoration: InputDecoration(
                      contentPadding:
                          const EdgeInsets.symmetric(vertical: 15.0),
                      border: OutlineInputBorder(
                        borderRadius: BorderRadius.circular(10.0),
                        borderSide: const BorderSide(
                          width: 0.5,
                        ),
                      ),
                      enabledBorder: OutlineInputBorder(
                        borderRadius: BorderRadius.circular(10.0),
                        borderSide: const BorderSide(
                          width: 0.5,
                          color: Colors.grey,
                        ),
                      ),
                      hintText: 'Password',
                      prefixIcon: const Icon(
                        Icons.lock,
                        size: 20.0,
                      ),
                      suffixIcon: IconButton(
                        onPressed: () {
                          setState(() {
                            isHidden = !isHidden;
                          });
                        },
                        icon: isHidden
                            ? const Icon(
                                Icons.visibility_off,
                                size: 20.0,
                              )
                            : const Icon(
                                Icons.visibility,
                                size: 20.0,
                              ),
                      ),
                    ),
                  ),
                  const SizedBox(
                    height: 20.0,
                  ),
                  TextFormField(
                    controller: reenterPasswordController,
                    textInputAction: TextInputAction.next,
                    keyboardType: TextInputType.text,
                    validator: (value) {
                      if (value == null || value != passwordController.text) {
                        return 'Please ensure that the passwords match';
                      } else {
                        return null;
                      }
                    },
                    obscureText: isHidden2,
                    enableSuggestions: false,
                    autocorrect: false,
                    decoration: InputDecoration(
                      contentPadding:
                          const EdgeInsets.symmetric(vertical: 15.0),
                      border: OutlineInputBorder(
                        borderRadius: BorderRadius.circular(10.0),
                        borderSide: const BorderSide(
                          width: 0.5,
                        ),
                      ),
                      enabledBorder: OutlineInputBorder(
                        borderRadius: BorderRadius.circular(10.0),
                        borderSide: const BorderSide(
                          width: 0.5,
                          color: Colors.grey,
                        ),
                      ),
                      hintText: 'Re-enter Password',
                      prefixIcon: const Icon(
                        Icons.lock,
                        size: 20.0,
                      ),
                      suffixIcon: IconButton(
                        onPressed: () {
                          setState(() {
                            isHidden2 = !isHidden2;
                          });
                        },
                        icon: isHidden2
                            ? const Icon(
                                Icons.visibility_off,
                                size: 20.0,
                              )
                            : const Icon(
                                Icons.visibility,
                                size: 20.0,
                              ),
                      ),
                    ),
                  ),
                  const SizedBox(
                    height: 20.0,
                  ),
                  CustomTextField(
                    controller: phoneNumberController,
                    textInputAction: TextInputAction.next,
                    keyboardType: TextInputType.phone,
                    validator: (value) {
                      if (value == null || value.isNotEmpty) {
                        return 'Please provide a valid phone number';
                      } else {
                        return null;
                      }
                    },
                    hintText: 'Phone Number',
                    prefixIcon: const Icon(
                      Icons.phone,
                      size: 20.0,
                    ),
                  ),
                  const SizedBox(
                    height: 20.0,
                  ),
                  CustomTextField(
                    controller: farmLocationController,
                    textInputAction: TextInputAction.done,
                    keyboardType: TextInputType.streetAddress,
                    validator: (value) {
                      if (value == null || value.isNotEmpty) {
                        return 'Please provide a valid farm location';
                      } else {
                        return null;
                      }
                    },
                    hintText: 'Farm Location',
                    prefixIcon: const Icon(
                      Icons.location_on_rounded,
                      size: 20.0,
                    ),
                  ),
                  const SizedBox(
                    height: 38.0,
                  ),
                  Center(
                    child: InkWell(
                      onTap: () {
                        if (_registerFormKey.currentState!.validate()) {
                          setState(() {
                            isLoading = true;
                          });
                          Future.delayed(const Duration(seconds: 2), () {
                            setState(() {
                              isLoading = false;
                            });
                            Navigator.pop(context);
                          });
                        }
                      },
                      child: Container(
                        height: isMediumMobile(context) ? 55 : 60,
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
                                  'Register',
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
                ],
              ),
            ),
            const SizedBox(
              height: 15.0,
            ),
            Center(
              child: Row(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  const Text(
                    'Already have an account?',
                    style: TextStyle(
                      fontSize: 18,
                      fontWeight: FontWeight.w200,
                    ),
                  ),
                  TextButton(
                    onPressed: () {
                      Navigator.pushReplacement(
                        context,
                        MaterialPageRoute(
                          builder: (_) => const LoginScreen(),
                        ),
                      );
                    },
                    child: Text(
                      'Login',
                      style: TextStyle(
                        fontSize: isMediumMobile(context) ? 18 : 20,
                        fontWeight: FontWeight.bold,
                        color: Theme.of(context).colorScheme.secondary,
                      ),
                    ),
                  )
                ],
              ),
            ),
          ],
        ),
      ),
    );
  }
}
