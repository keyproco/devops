FROM coredns/coredns:latest
EXPOSE 53
VOLUME [ "/etc/dns" ]

ENTRYPOINT [ "/coredns" ]

CMD ["--conf", "/root/Corefile"]