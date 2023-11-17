import 'package:flutter/material.dart';
import 'package:smart_farming/bottom_navbar.dart';
import 'package:smart_farming/register.dart';
import 'package:smart_farming/screen_constants.dart';
import 'package:smart_farming/services/login.dart';
import 'package:smart_farming/textfield_widget.dart';

class LoginScreen extends StatefulWidget {
  const LoginScreen({super.key});

  @override
  State<LoginScreen> createState() => _LoginScreenState();
}

class _LoginScreenState extends State<LoginScreen> {
  final _loginFormKey = GlobalKey<FormState>();
  bool loginLoading = false;
  final TextEditingController emailController = TextEditingController();
  final TextEditingController passwordController = TextEditingController();
  bool isHidden = true;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Padding(
        padding: const EdgeInsets.all(20),
        child: ListView(
          children: [
            Column(
              crossAxisAlignment: CrossAxisAlignment.center,
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                SizedBox(
                  height: isMediumMobile(context)
                      ? MediaQuery.of(context).size.height * 0.05
                      : MediaQuery.of(context).size.height * 0.12,
                ),
                Container(
                  height: isMediumMobile(context)
                      ? 120
                      : MediaQuery.of(context).size.height * 0.15,
                  width: isMediumMobile(context)
                      ? 120
                      : MediaQuery.of(context).size.height * 0.15,
                  decoration: BoxDecoration(
                    borderRadius: BorderRadius.circular(
                      isMediumMobile(context)
                          ? 20
                          : MediaQuery.of(context).size.height * 0.03,
                    ),
                    border: Border.all(
                      color: Theme.of(context).colorScheme.primary,
                      width: 2.0,
                    ),
                  ),
                  child: ClipRRect(
                    borderRadius: BorderRadius.circular(
                      isMediumMobile(context)
                          ? 20
                          : MediaQuery.of(context).size.height * 0.03,
                    ),
                    child: Image.asset(
                      'assets/images/logo.png',
                      fit: BoxFit.cover,
                    ),
                  ),
                ),
                SizedBox(
                  height: isMediumMobile(context)
                      ? 15
                      : MediaQuery.of(context).size.height * 0.02,
                ),
                Text(
                  'Smart Farming',
                  style: TextStyle(
                    fontWeight: FontWeight.w500,
                    fontSize: isMediumMobile(context) ? 25 : 28,
                    color: Theme.of(context).colorScheme.primary,
                  ),
                ),
              ],
            ),
            const SizedBox(
              height: 30,
            ),
            Form(
              key: _loginFormKey,
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  const Text(
                    'Login',
                    style: TextStyle(
                      fontWeight: FontWeight.bold,
                      fontSize: 30,
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
                    textInputAction: TextInputAction.done,
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
                    height: 38.0,
                  ),
                  Center(
                    child: InkWell(
                      onTap: () {
                        if (_loginFormKey.currentState!.validate()) {
                          setState(() {
                            loginLoading = true;
                          });
                          login(
                            context,
                            emailController.text,
                            passwordController.text,
                          );
                          Future.delayed(const Duration(seconds: 1), () {
                            setState(() {
                              loginLoading = false;
                            });
                          });
                        }
                      },
                      child: Container(
                        height: 55.0,
                        decoration: BoxDecoration(
                          color: Theme.of(context).colorScheme.secondary,
                          border: Border.all(
                            color: Theme.of(context).colorScheme.secondary,
                          ),
                          borderRadius: BorderRadius.circular(15.0),
                        ),
                        child: Center(
                          child: loginLoading
                              ? const SizedBox(
                                  height: 30.0,
                                  width: 30.0,
                                  child: CircularProgressIndicator(
                                    color: Colors.white,
                                  ),
                                )
                              : const Text(
                                  'Login',
                                  style: TextStyle(
                                    fontSize: 18.0,
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
                    'New to Smart Farming?',
                    style: TextStyle(
                      fontSize: 18,
                      fontWeight: FontWeight.w200,
                    ),
                  ),
                  TextButton(
                    onPressed: () {
                      Navigator.push(
                        context,
                        MaterialPageRoute(
                          builder: (_) => const RegistrationScreen(),
                        ),
                      );
                    },
                    child: Text(
                      'Register',
                      style: TextStyle(
                        fontSize: 18,
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
