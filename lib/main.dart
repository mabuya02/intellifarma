import 'package:flutter/material.dart';
import 'package:smart_farming/login.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Smart Farming',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(
          seedColor: const Color(0xff054d3b),
          primary: const Color(0xff054d3b),
          secondary: const Color(0xff008000),
          background: const Color(0xffffffff),
          surfaceTint: const Color(0xffffffff),
          error: Colors.red,
        ),
        useMaterial3: true,
      ),
      home: const LoginScreen(),
    );
  }
}
