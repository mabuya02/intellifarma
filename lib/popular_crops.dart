import 'package:flutter/material.dart';
import 'package:persistent_bottom_nav_bar/persistent_tab_view.dart';
import 'package:smart_farming/login.dart';
import 'package:smart_farming/screen_constants.dart';
import 'package:smart_farming/webview.dart';

class PopularCropsScreen extends StatefulWidget {
  const PopularCropsScreen({super.key});

  @override
  State<PopularCropsScreen> createState() => _PopularCropsScreenState();
}

class _PopularCropsScreenState extends State<PopularCropsScreen> {
  List popularCrops = [
    {
      "image": "assets/images/corn.jpg",
      "name": "Corn",
      "description": "Corn is a cereal crop that is part of the grass family.",
      "rating": "4.5",
      "video": "https://youtu.be/WNUNq4QJ-CM?si=5yyKiTC303f9rgIe"
    },
    {
      "image": "assets/images/rice.jpg",
      "name": "Rice",
      "description":
          "Rice is the seed of the grass species Oryza sativa or less commonly Oryza glaberrima.",
      "rating": "4.2",
      "video": "https://youtu.be/J_mMS3EkHok?si=eHBBhhiBTZo0gd16"
    },
    {
      "image": "assets/images/wheat.jpg",
      "name": "Wheat",
      "description":
          "Wheat is a grass widely cultivated for its seed, a cereal grain which is a worldwide staple food.",
      "rating": "4.4",
      "video": "https://youtu.be/fkO3EhG7v3c?si=x_KvpQ0gPw3CfS2p"
    },
    {
      "image": "assets/images/soybean.jpg",
      "name": "Soybean",
      "description":
          "The soybean or soya bean is a species of legume native to East Asia, widely grown for its edible bean, which has numerous uses.",
      "rating": "4.8",
      "video": "https://youtu.be/C8yjMPUV3Vw?si=ZuO-gPIZ8xncOFdp"
    }
  ];
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
                size: 30,
              ),
            ),
          ],
        ),
      ),
      body: SingleChildScrollView(
        child: Padding(
          padding: const EdgeInsets.all(10.0),
          child: Column(
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
                height: 10.0,
              ),
              const Center(
                child: Text(
                  'Popular Crops',
                  style: TextStyle(
                    fontWeight: FontWeight.w500,
                    fontSize: 24,
                  ),
                ),
              ),
              const SizedBox(
                height: 10,
              ),
              ListView.separated(
                shrinkWrap: true,
                physics: const NeverScrollableScrollPhysics(),
                itemBuilder: (context, index) {
                  var crop = popularCrops[index];
                  return GestureDetector(
                    onTap: () {
                      PersistentNavBarNavigator.pushNewScreen(
                        context,
                        screen: VideoWebview(
                            videoLink: crop["video"],
                            cropType: crop["name"],
                          ),
                        withNavBar: false, // OPTIONAL VALUE. True by default.
                        pageTransitionAnimation:
                            PageTransitionAnimation.cupertino,
                      );
                    },
                    child: ListTile(
                      leading: CircleAvatar(
                        radius: 30.0,
                        backgroundImage: Image.asset(
                          crop["image"],
                          fit: BoxFit.cover,
                        ).image,
                      ),
                      title: Text(
                        crop["name"],
                        style: const TextStyle(
                          fontWeight: FontWeight.w500,
                          fontSize: 20,
                          color: Colors.black,
                        ),
                      ),
                      subtitle: Column(
                        crossAxisAlignment: CrossAxisAlignment.start,
                        children: [
                          Text(
                            crop["description"],
                            style: const TextStyle(
                              fontWeight: FontWeight.w400,
                              fontSize: 16,
                              color: Colors.black54,
                            ),
                          ),
                          const SizedBox(
                            height: 5,
                          ),
                          Row(
                            children: [
                              Text(
                                crop["rating"],
                                style: const TextStyle(
                                  fontWeight: FontWeight.w400,
                                  fontSize: 16,
                                ),
                              ),
                              const SizedBox(
                                width: 5,
                              ),
                              const Icon(
                                Icons.star,
                                color: Colors.amber,
                                size: 20,
                              ),
                            ],
                          ),
                          const SizedBox(
                            height: 5,
                          ),
                          Text(
                            'Tap to watch video',
                            style: TextStyle(
                              fontWeight: FontWeight.w400,
                              fontSize: 16,
                              color: Theme.of(context).colorScheme.primary,
                            ),
                          ),
                        ],
                      ),
                    ),
                  );
                },
                separatorBuilder: (context, index) {
                  return const Divider();
                },
                itemCount: popularCrops.length,
              ),
            ],
          ),
        ),
      ),
    );
  }
}
