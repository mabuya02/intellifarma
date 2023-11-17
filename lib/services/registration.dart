// To parse this JSON data, do
//
//     final registration = registrationFromJson(jsonString);

import 'dart:convert';
import 'package:http/http.dart' as http;
import 'package:flutter/material.dart';
import 'package:smart_farming/constants/constants.dart';
import 'package:smart_farming/login.dart';

Registration registrationFromJson(String str) =>
    Registration.fromJson(json.decode(str));

String registrationToJson(Registration data) => json.encode(data.toJson());

class Registration {
  String firstName;
  String lastName;
  String password;
  String email;
  int roleId;
  String contactNumber;
  String farmLocation;
  String status;

  Registration({
    required this.firstName,
    required this.lastName,
    required this.password,
    required this.email,
    required this.roleId,
    required this.contactNumber,
    required this.farmLocation,
    required this.status,
  });

  factory Registration.fromJson(Map<String, dynamic> json) => Registration(
        firstName: json["First_name"],
        lastName: json["last_name"],
        password: json["password"],
        email: json["email"],
        roleId: json["role_id"],
        contactNumber: json["contact_number"],
        farmLocation: json["farm_location"],
        status: json["status"],
      );

  Map<String, dynamic> toJson() => {
        "First_name": firstName,
        "last_name": lastName,
        "password": password,
        "email": email,
        "role_id": roleId,
        "contact_number": contactNumber,
        "farm_location": farmLocation,
        "status": status,
      };
}

// // Create secure token storage for storing the token
// final tokenStorage = FlutterSecureStorage();
// Future<String> retrieveToken() async {
//   String? value = await tokenStorage.read(key: 'accessToken');
//   return value.toString();
// }

// This function logs in the user by sending a POST request to the server.
Future register(BuildContext context, String username, String password) async {
  try {
    String base = baseUri;
    String register = registerUri;
    final response = await http.post(
      Uri.parse("$base$register"),
      headers: <String, String>{
        'Content-Type': 'application/json; charset=UTF-8',
      },
      body: jsonEncode(<String, dynamic>{
        'username': username,
        'password': password,
      }),
    );

    String result = jsonDecode(response.body)['message'];
    if (response.statusCode == 200) {
      final Map<String, dynamic> userResult = jsonDecode(response.body);

      return Navigator.pushAndRemoveUntil(
        context,
        MaterialPageRoute(
          builder: (context) => LoginScreen(),
        ),
        (route) => false,
      );
    } else if (result == "Invalid Login credentials") {
      var error = ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(
          content: const Text(
            'Invalid Login credentials',
            style: TextStyle(
              color: Colors.white,
              fontWeight: FontWeight.w500,
            ),
          ),
          backgroundColor: Theme.of(context).colorScheme.error,
          duration: const Duration(seconds: 1),
          shape: RoundedRectangleBorder(
            borderRadius: BorderRadius.all(
              Radius.circular(MediaQuery.of(context).size.width * 0.02),
            ),
          ),
          behavior: SnackBarBehavior.floating,
        ),
      );

      return error;
    } else {
      var error = ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(
          content: const Text(
            'Failed to Login User',
            style: TextStyle(
              color: Colors.white,
              fontWeight: FontWeight.w500,
            ),
          ),
          backgroundColor: Theme.of(context).colorScheme.error,
          duration: const Duration(seconds: 1),
          shape: RoundedRectangleBorder(
            borderRadius: BorderRadius.all(
              Radius.circular(MediaQuery.of(context).size.width * 0.02),
            ),
          ),
          behavior: SnackBarBehavior.floating,
        ),
      );

      return error;
    }
  } catch (e) {
    print(e.toString());
    throw Exception('Failed to Login User: $e');
  }
}
